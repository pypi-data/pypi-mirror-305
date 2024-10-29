#!/usr/bin/env python3

import json
import os 

import numpy as np
import pandas as pd
import torch
from torch import optim
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm

from typing import Iterable, Literal

from anndata import AnnData

from cobra_ai.model.vanilla_vae import vanillaVAE
from cobra_ai.module.modules import Classifier
from cobra_ai.module.utils import split_adata, FastTensorDataLoader
from cobra_ai.module.metrics import knn_purity

from ray import train


"""VAE with ontology in decoder"""

class advVAE(vanillaVAE):
    """
    This class is a VAE implementation of CPA (Lotfollahi et al, 2023).

    Parameters
    ----------
    adata
        anndata object that has been preprocessed with setup_anndata function
    hidden_layers_class
        number of hidden layers
    neurons_per_class_layer
        number of neurons in a hidden layer
    use_batch_norm_class
        Whether to have `BatchNorm` layers or not in encoder
    use_layer_norm_class
        Whether to have `LayerNorm` layers or not in encoder
    use_activation_class
        Whether to have layer activation or not in encoder
    activation_fn_class
        Which activation function to use in encoder
    bias_class
        Whether to learn bias in linear layers or not in encoder
    inject_covariates_class
        Whether to inject covariates in each layer (True), or just the first (False) of encoder
    drop_class
        dropout rate in encoder
    
    Inherited Parameters (should be passed as dictionary to **kwargs)
    --------------------
    use_batch_norm_enc
        Whether to have `BatchNorm` layers or not in encoder
    use_layer_norm_enc
        Whether to have `LayerNorm` layers or not in encoder
    use_activation_enc
        Whether to have layer activation or not in encoder
    activation_fn_enc
        Which activation function to use in encoder
    bias_enc
        Whether to learn bias in linear layers or not in encoder
    inject_covariates_enc
        Whether to inject covariates in each layer (True), or just the first (False) of encoder
    drop_enc
        dropout rate in encoder
    z_drop
        dropout rate for latent space 
    use_batch_norm_dec
        Whether to have `BatchNorm` layers or not in decoder
    use_layer_norm_dec
        Whether to have `LayerNorm` layers or not in decoder
    use_activation_dec
        Whether to have layer activation or not in decoder
    activation_fn_dec
        Which activation function to use in decoder
    bias_dec
        Whether to learn bias in linear layers or not in decoder
    inject_covariates_dec
        Whether to inject covariates in each layer (True), or just the last (False) of decoder
    drop_dec
        dropout rate in decoder
    """

    @classmethod
    def load(cls, adata: AnnData, modelpath: str):
        with open(modelpath + '/model_params.json', 'r') as fp:
            params = json.load(fp)
        if params['activation_fn_enc'] is not None:
            params['activation_fn_enc'] = eval(params['activation_fn_enc'])
        if params['activation_fn_dec'] is not None:
            params['activation_fn_dec'] = eval(params['activation_fn_dec'])
        if params['activation_fn_class'] is not None:
            params['activation_fn_class'] = eval(params['activation_fn_class'])
        model = cls(adata, **params) 
        checkpoint = torch.load(modelpath + '/best_model.pt',
                            map_location = torch.device(model.device))
        model.load_state_dict(checkpoint['model_state_dict'], strict=False)
        return model
    
    def __init__(self, 
                 adata: AnnData, 
                 hidden_layers_class: int = 2,
                 neurons_per_class_layer: int = 64,
                 use_batch_norm_class: bool = True,
                 use_layer_norm_class: bool = False,
                 use_activation_class: bool = True,
                 activation_fn_class: nn.Module = nn.ReLU,
                 bias_class: bool = True,
                 inject_covariates_class: bool = False,
                 drop_class: float = 0.2,
                 **kwargs):
        super().__init__(adata, **kwargs)

        class_params = {'hidden_layers_class': hidden_layers_class,
                        'neurons_per_class_layer': neurons_per_class_layer,
                        'use_batch_norm_class': use_batch_norm_class,
                        'use_layer_norm_class': use_layer_norm_class,
                        'use_activation_class': use_activation_class,
                        'activation_fn_class': str(activation_fn_class).split("'")[1] if activation_fn_class is not None else activation_fn_class,
                        'bias_class': bias_class,
                        'inject_covariates_class': inject_covariates_class,
                        'drop_class': drop_class}
        self.params.update(class_params)

        
        # set up covariates
        self.cobra_covs = adata.obsm['_cobra_categorical_covs'] if '_cobra_categorical_covs' in adata.obsm.keys() else None
        if self.cobra_covs is None:
            raise ValueError('Please specify cpa_keys in setup_anndata_vanillavae to run the model.')

        self.cov_dict = {}
        for cov in self.cobra_covs.columns:
            self.cov_dict[cov] = dict(zip(adata.obs.loc[:,cov].tolist(), self.cobra_covs.loc[:,cov].tolist()))

        # embedding of covars
        self.covars_embeddings = nn.ModuleDict(
            {
                key: torch.nn.Embedding(len(self.cov_dict[key]), self.latent_dim)
                for key in self.cov_dict.keys()
            }
        )
        
        # covars classifiers
        self.covars_classifiers = nn.ModuleDict(
            {
                key: Classifier(in_features = self.latent_dim,
                                n_classes = len(self.cov_dict[key]),
                                n_cat_list = self.n_cat_list,
                                hidden_layers = hidden_layers_class,
                                neurons_per_layer = neurons_per_class_layer,
                                use_batch_norm = use_batch_norm_class,
                                use_layer_norm = use_layer_norm_class,
                                use_activation = use_activation_class,
                                activation_fn = activation_fn_class,
                                bias = bias_class,
                                inject_covariates = inject_covariates_class,
                                drop = drop_class)
                for key in self.cov_dict.keys()
            }
        )

        self.to(self.device)

    def _get_embedding(self, x: torch.tensor, cat_list: Iterable[torch.tensor], cov_list: Iterable[torch.tensor], mixup_lambda=1):
        """
        Generates latent space embedding.

        Parameters
        ----------
        x
            torch.tensor of shape (minibatch, in_features)
        cat_list
            Iterable of torch.tensors containing the category memberships
            shape of each tensor is (minibatch, 1)
        cov_list
            Iterable of torch.tensors containing the covs to delineate in 
            latent space 
        mixup_lambda
            coefficient for adversarial training
        """
        # data mixup for adversarial training
        batch_size = x.size()[0]
        if mixup_lambda  < 1:
            index = torch.randperm(batch_size).to(x.device)
            x = mixup_lambda * x + (1. - mixup_lambda) * x[index, :]
        else:
            index = torch.arange(0,batch_size).to(x.device)

        # encoding
        mu, log_var = self.encoder(x, cat_list)
            
        # sample from latent space
        z_basal = self.reparameterize(mu, log_var)
        if self.use_activation_lat and self.use_activation_dec:
            z_basal = self.activation_fn_dec()(z_basal)

        # covariate encoding
        covars_embeddings = {}
        for i, key in enumerate(self.covars_embeddings.keys()):
            cov_embed = self.covars_embeddings[key](cov_list[i].long().squeeze())
            cov_mix_embed = self.covars_embeddings[key](cov_list[i].long().squeeze()[index])
            covars_embeddings[key] = mixup_lambda * cov_embed + (1. - mixup_lambda) * cov_mix_embed

        # create different z's
        z_cov = {}
        z_total = z_basal.clone()
        for key in covars_embeddings.keys():
            z_cov['z_' + key] = (z_basal + covars_embeddings[key])
            z_total += covars_embeddings[key]

        z_dict = dict(z_basal=z_basal)
        z_dict.update(z_cov, z_total=z_total)

        return z_dict, mu, log_var
  
    def forward(self, x: torch.tensor, cat_list: Iterable[torch.tensor], cov_list: Iterable[torch.tensor], mixup_lambda: float):
        """
        Forward computation on minibatch of samples.
        
        Parameters
        ----------
        x
            torch.tensor of shape (minibatch, in_features)
        cat_list
            Iterable of torch.tensors containing the category memberships
            shape of each tensor is (minibatch, 1)
        cov_list
            Iterable of torch.tensors containing the covs to delineate in 
            latent space 
        mixup_lambda
            coefficient for adversarial training
        """
        # inference
        zdict, mu, log_var = self._get_embedding(x, cat_list, cov_list, mixup_lambda)

        # decoding
        reconstruction = self.decoder(zdict['z_total'], cat_list)
            
        return zdict, mu, log_var, reconstruction


    def adv_forward(self, z: torch.tensor, cat_list: Iterable[torch.tensor], compute_penalty=False):
        """
        Forward computation on minibatch of samples for z_basal.
        
        Parameters
        ----------
        z
            torch.tensor of shape (minibatch, in_features)
        cat_list
            Iterable of torch.tensors containing the category memberships
            shape of each tensor is (minibatch, 1)
        """
        if compute_penalty:
            z = z.requires_grad_(True)

        # covariate classifiers on z_basal
        covars_pred = {}
        for key in self.covars_classifiers.keys():
            covar_pred = self.covars_classifiers[key](z, cat_list)
            covars_pred[key] = covar_pred
        
        if compute_penalty:
            penalty = 0.0
            # Penalty losses
            for key in self.covars_classifiers.keys():
                pen = (
                    torch.autograd.grad(
                        covars_pred[key].sum(),
                        z,
                        create_graph=True,
                        retain_graph=True,
                        only_inputs=True,
                    )[0].pow(2).mean()
                )
                penalty += pen
            covars_pred['penalty'] = penalty
        
        return covars_pred

    def clf_loss(self, class_output, y, cov: str, mode='train', run=None):
        """
        Calculates loss of a covariate classifier
        """
        class_loss = nn.CrossEntropyLoss()
        clf_loss = class_loss(class_output, y)
        if run is not None:
            run["metrics/" + mode + "/" + cov + "_clf_loss"].log(clf_loss)
        return clf_loss

    def train_round(self, 
                    dataloader: FastTensorDataLoader, 
                    kl_coeff: float, 
                    adv_coeff: float,
                    pen_coeff: float,
                    mixup_lambda: float,
                    adv_step: int,
                    optimizer_vae: optim.Optimizer, 
                    optimizer_adv: optim.Optimizer,
                    run=None):
        """
        Parameters
        ----------
        dataloader
            pytorch dataloader instance with training data
        kl_coeff 
            coefficient for weighting Kullback-Leibler loss
        adv_coeff 
            coefficient for weighting classifier
        pen_coeff
            coefficient for weighting gradient penalty
        mixup_lambda
            coefficient for data mixing
        adv_step:
            after how many minibatches the discriminators should be updated
        optimizer_vae
            optimizer for training the VAE
        optimizer_adv
            optimizer for training the adversarial component
        run
            Neptune run if training is to be logged
        """
        # set to train mode
        self.train()

        # initialize running losses
        running_loss_vae = 0.0
        running_loss_adv = 0.0

        # init purity
        purity = 0.0

        # iterate over dataloader for training
        for i, minibatch in enumerate(dataloader):

            # move minibatch to device
            data = torch.tensor(minibatch[0].todense(), dtype=torch.float32).to(self.device)
            cat_list = torch.split(minibatch[1].T.to(self.device), 1)
            cov_list = torch.split(minibatch[2].T.to(self.device), 1)

            # VAE optimizer
            optimizer_vae.zero_grad()

            # forward step generator
            z_dict, mu, logvar, reconstruction = self.forward(data, cat_list, cov_list, mixup_lambda)
            z_basal = z_dict["z_basal"]
            covars_pred = self.adv_forward(z_basal, cat_list)
            vae_loss = self.vae_loss(reconstruction, mu, logvar, data, kl_coeff, mode='train', run=run)
            adv_loss = 0.0
            for i, vals in enumerate(cov_list):
                cov = list(self.cov_dict.keys())[i]
                cov_loss = self.clf_loss(covars_pred[cov], vals.long().squeeze(), cov=cov, mode='train', run=run)
                adv_loss += cov_loss
            loss = vae_loss - adv_coeff * adv_loss
            running_loss_vae += loss.item()

            # backward propagation
            loss.backward()
            optimizer_vae.step()

            # adversarial training
            if i % adv_step == 0:
                # adversarial optimizer
                optimizer_adv.zero_grad()

                # forward step discriminator
                covars_pred = self.adv_forward(z_basal.detach(), cat_list, compute_penalty=True)
                adv_loss = 0.0
                for i, vals in enumerate(cov_list):
                    cov = list(self.cov_dict.keys())[i]
                    cov_loss = self.clf_loss(covars_pred[cov], vals.long().squeeze(), cov=cov, mode='train', run=run)
                    adv_loss += cov_loss
                loss = adv_loss + pen_coeff * covars_pred['penalty']
                running_loss_adv += loss

                # backward propagation
                loss.backward()
                optimizer_adv.step()

            # compute KNN purity
            cov_purity = []
            for i, vals in enumerate(cov_list):
                cov = list(self.cov_dict.keys())[i]
                cov_purity.append(knn_purity(z_basal.to('cpu').detach().numpy(), vals.long().squeeze().to('cpu').detach().numpy()))
            purity += np.mean(cov_purity)

        # compute avg training loss
        train_loss_vae = running_loss_vae/len(dataloader)
        train_loss_adv = running_loss_adv/len(dataloader)

        # compute average purity
        avg_purity = purity/len(dataloader)

        return train_loss_vae, train_loss_adv, avg_purity

    @torch.no_grad()
    def val_round(self, 
                  dataloader: FastTensorDataLoader, 
                  kl_coeff: float, 
                  adv_coeff: float,
                  run=None):
        """
        Parameters
        ----------
        dataloader
            pytorch dataloader instance with training data
        kl_coeff
            coefficient for weighting Kullback-Leibler loss
        adv_coeff 
            coefficient for weighting classifier
        run
            Neptune run if training is to be logged
        """
        # set to eval mode
        self.eval()
        #mixup_lambda=0

        # initialize running losses
        running_loss_vae = 0.0

        # init purity
        purity = 0.0

        # iterate over dataloader for validation
        for i, minibatch in enumerate(dataloader):

            # move minibatch to device
            data = torch.tensor(minibatch[0].todense(), dtype=torch.float32).to(self.device)
            cat_list = torch.split(minibatch[1].T.to(self.device), 1)
            cov_list = torch.split(minibatch[2].T.to(self.device), 1)

            # forward step generator
            z_dict, mu, logvar, reconstruction = self.forward(data, cat_list, cov_list, mixup_lambda=1)
            z_basal = z_dict["z_basal"]
            covars_pred = self.adv_forward(z_basal, cat_list)
            vae_loss = self.vae_loss(reconstruction, mu, logvar, data, kl_coeff, mode='val', run=run)
            adv_loss = 0.0
            for i, vals in enumerate(cov_list):
                cov = list(self.cov_dict.keys())[i]
                cov_loss = self.clf_loss(covars_pred[cov], vals.long().squeeze(), cov=cov, mode='val', run=run)
                adv_loss += cov_loss
            loss = vae_loss - adv_coeff * adv_loss
            running_loss_vae += loss.item()

            # compute KNN purity
            cov_purity = []
            for i, vals in enumerate(cov_list):
                cov = list(self.cov_dict.keys())[i]
                cov_purity.append(knn_purity(z_basal.to('cpu').detach().numpy(), vals.long().squeeze().to('cpu').detach().numpy()))
            purity += np.mean(cov_purity)
        
        # compute avg training loss
        val_loss_vae = running_loss_vae/len(dataloader)

        # compute average purity
        avg_purity = purity/len(dataloader)

        return val_loss_vae, avg_purity
    

    def train_model(self, 
                    modelpath: str, 
                    train_size: float = 0.9,
                    seed: int = 42,
                    lr_vae: float=1e-4, 
                    lr_adv: float=1e-4,
                    kl_coeff: float=1e-4, 
                    adv_coeff: float=1e2,
                    pen_coeff: float=2.0,
                    mixup_lambda: float=1.0,
                    adv_step: int=1,
                    batch_size: int=128, 
                    optimizer: optim.Optimizer = optim.AdamW,
                    epochs: int=1000, 
                    tune_params: bool=False,
                    run=None):
        """
        Parameters
        ----------
        modelpath
            path to a folder where to store the params and the best model 
        train_size
            which percentage of samples to use for training
        seed
            seed for the train-val split
        lr_vae
            learning rate for the VAE optimizer
        lr_adv
            learning rate for the adversarial optimizer
        kl_coeff
            Kullback Leibler loss coefficient
        adv_coeff 
            coefficient for weighting classifier
        pen_coeff
            coefficient for weighting gradient penalty
        mixup_lambda
            coefficient for adversarial training
        adv_step
            after how many minibatches the discriminators should be updated
        batch_size
            size of minibatches
        optimizer
            which optimizer to use
        epochs
            over how many epochs to train
        run
            passed here if logging to Neptune should be carried out
        """

        if os.path.isfile(modelpath + '/best_model.pt'):
            print("A model already exists in the specified directory and will be overwritten.")
            
        # save train params
        train_params = {'train_size': train_size,
                        'seed': seed,
                        'lr_vae': lr_vae,
                        'lr_adv': lr_adv,
                        'kl_coeff': kl_coeff,
                        'adv_coeff': adv_coeff,
                        'pen_coeff': pen_coeff,
                        'mixup_lambda': mixup_lambda,
                        'adv_step': adv_step,
                        'batch_size': batch_size,
                        'optimizer': str(optimizer).split("'")[1],
                        'epochs': epochs
                        }
        with open(modelpath + '/train_params.json', 'w') as fp:
            json.dump(train_params, fp, indent=4)

        if run is not None:
            run["train_parameters"] = train_params

        # save model params
        with open(modelpath + '/model_params.json', 'w') as fp:
            json.dump(self.params, fp, indent=4)

        if run is not None:
            run["model_parameters"] = self.params

        # train-val split
        train_adata, val_adata = split_adata(self.adata, 
                                             train_size = train_size,
                                             seed = seed)

        train_batch = self._cov_tensor(train_adata)
        val_batch = self._cov_tensor(val_adata)

        train_covs = torch.tensor(train_adata.obsm['_cobra_categorical_covs'].to_numpy())
        val_covs = torch.tensor(val_adata.obsm['_cobra_categorical_covs'].to_numpy())

        # generate dataloaders
        trainloader = FastTensorDataLoader(train_adata.X, 
                                           train_batch,
                                           train_covs,
                                         batch_size=batch_size, 
                                         shuffle=True)
        valloader = FastTensorDataLoader(val_adata.X, 
                                         val_batch,
                                         val_covs,
                                        batch_size=batch_size, 
                                        shuffle=False)

        purity_min = 1.0
        val_loss_min = float('inf')
        optimizer_vae = optimizer(list(self.encoder.parameters()) + list(self.decoder.parameters()) + list(self.covars_embeddings.parameters()), lr = lr_vae)
        optimizer_adv = optimizer(self.covars_classifiers.parameters(), lr = lr_adv)

        for epoch in tqdm(range(epochs)):
            print(f"Epoch {epoch+1} of {epochs}")
            train_epoch_loss_vae, train_epoch_loss_adv, train_knn_purity = self.train_round(trainloader, 
                                                                                            kl_coeff, 
                                                                                            adv_coeff, 
                                                                                            pen_coeff, 
                                                                                            mixup_lambda, 
                                                                                            adv_step, 
                                                                                            optimizer_vae, 
                                                                                            optimizer_adv, 
                                                                                            run)
            val_epoch_loss_vae, val_knn_purity = self.val_round(valloader, 
                                                                kl_coeff, 
                                                                adv_coeff,
                                                                run)
            
            if run is not None:
                run["metrics/train/loss_vae"].log(train_epoch_loss_vae)
                run["metrics/train/loss_adv"].log(train_epoch_loss_adv)
                run["metrics/train/knn_purity"].log(train_knn_purity)
                run["metrics/val/loss_vae"].log(val_epoch_loss_vae)
                run["metrics/val/knn_purity"].log(val_knn_purity)
                
            if val_epoch_loss_vae < val_loss_min:
                print('New best model!')
                torch.save({
                    'epoch': epoch,
                    'model_state_dict': self.state_dict(),
                    'optimizer_vae_state_dict': optimizer_vae.state_dict(),
                    'optimizer_adv_state_dict': optimizer_adv.state_dict(),
                    'knn_purity': val_knn_purity,
                }, modelpath + '/best_model.pt')
                val_loss_min = val_epoch_loss_vae
                
            if tune_params:
                train.report({"purity": val_knn_purity})

    @torch.no_grad()
    def _pass_data(self, x, cat_list, cov_list):
        """
        Passes data through the model.

        Parameters
        ----------
        x
            torch.tensor of shape (minibatch, in_features)
        cat_list
            Iterable of torch.tensors containing the category memberships
            shape of each tensor is (minibatch, 1)
        cov_list
            Iterable of torch.tensors containing the covs to delineate in 
            latent space 
        """

        # set to eval mode
        self.eval()

        # get latent space embedding dict
        zdict = self._get_embedding(x, cat_list, cov_list)
        dict_keys = list(zdict.keys())

        # pass forward the different z's
        rec_dict = {}

        for z_key in dict_keys:
            z = zdict[z_key].clone()
            
            # pass data through model
            reconstruction = self.decoder(z, cat_list)

            # return reconstructed gene values
            rec_dict[z_key] = reconstruction

        return rec_dict
                

    @torch.no_grad()
    def _run_batches(self, adata: AnnData, retrieve: Literal['latent', 'rec']):
        """
        Runs batches of a dataloader through encoder or complete VAE and collects results.

        Parameters
        ----------
        latent
            whether to retrieve latent space embedding (True) or reconstructed values (False)
        """
        self.eval()

        if adata is None:
            adata = self.adata

        batch = self._cov_tensor(adata)
        covs = torch.tensor(adata.obsm['_cobra_categorical_covs'].to_numpy())

        dataloader = FastTensorDataLoader(adata.X, 
                                          batch,
                                          covs,
                                         batch_size=128, 
                                         shuffle=False)

        res = []
        for minibatch in dataloader:
            x = torch.tensor(minibatch[0].todense(), dtype=torch.float32).to(self.device)
            cat_list = torch.split(minibatch[1].T.to(self.device), 1)
            cov_list = torch.split(minibatch[2].T.to(self.device), 1)
            if retrieve == 'latent':
                result, _, _ = self._get_embedding(x, cat_list, cov_list)
            else:
                result = self._pass_data(x, cat_list, cov_list)
            result_avg = {k: v.to('cpu').detach().numpy() for k, v in result.items()}
            res.append(result_avg)

        res_out = {}
        key_list = list(res[0].keys())
        for key in key_list:
            res_key = np.vstack([r[key] for r in res])
            res_out[key] = res_key

        return res_out
    
    @torch.no_grad()
    def to_latent(self, adata: AnnData=None):
        """
        Retrieves different representations of z.

        Parameters
        ----------
        adata
            AnnData object that was processed with setup_anndata
        """
        self.eval()
        res = self._run_batches(adata, 'latent')
        return res


    @torch.no_grad()
    def get_reconstructed_values(self, adata: AnnData=None):
        """
        Retrieves reconstructed values from output layer.

        Parameters
        ----------
        adata
            AnnData object that was processed with setup_anndata
        """
        self.eval()
        res = self._run_batches(adata, 'rec')
        return res

    
    @torch.no_grad()
    def perturbation(self, adata: AnnData=None, genes: list=[], values: list=[]):
        """
        Retrieves pathway activities or reconstructed gene values after performing in silico perturbation.

        Parameters
        ----------
        adata
            AnnData object that was processed with setup_anndata
        genes
            a list of genes to perturb
        values
            list with new values, same length as genes
        """
        self.eval()
        
        if adata is not None:
            if '_ontovae' not in adata.uns.keys():
                raise ValueError('Please run cobra_ai.module.utils.setup_anndata first.')
            pdata = adata.copy()
        else:
            pdata = self.adata.copy()

        # get indices of the genes in list
        gindices = [pdata.uns['_ontovae']['genes'].index(g) for g in genes]

        # replace their values
        for i in range(len(genes)):
            pdata.X[:,gindices[i]] = values[i]

        # run perturbed data through network
        res = self._run_batches(pdata, 'rec')

        return res
    
        