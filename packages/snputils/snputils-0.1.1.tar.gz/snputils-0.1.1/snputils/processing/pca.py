__author__ = "davidbonet"

"""Principal components analysis (PCA) with PyTorch tensors, compatible with GPU.
   - Up to 25x faster than sklearn.decomposition.PCA when running on GPU.
   - Works on GPU with CUDA 10.2, does not seem to work with CUDA 11.3
     - Recommended conda install: conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
"""

import torch
import numpy as np
from sklearn.decomposition import PCA

def svd_flip(u, v, u_based_decision=True):
    """Sign correction to ensure deterministic output from SVD.

    Adjusts the columns of u and the rows of v such that the loadings in the
    columns in u that are largest in absolute value are always positive.
    """
    if u_based_decision:
        # columns of u, rows of v
        max_abs_cols = torch.argmax(torch.abs(u), axis=0)
        signs = torch.sign(u[max_abs_cols, range(u.shape[1])])
        u *= signs
        v *= signs[:, None]
    else:
        # rows of v, columns of u
        max_abs_rows = torch.argmax(torch.abs(v), axis=1)
        signs = torch.sign(v[range(v.shape[0]), max_abs_rows])
        u *= signs
        v *= signs[:, None]

    return u, v


class TorchPCA():
    def __init__(self, n_components=None, fitting="full"):
        self.n_components = n_components
        self.fitting = fitting
    
    def _fit(self, X):
        if self.n_components is None:
            if self.fitting == "lowrank":
                n_components = min(X.shape)
            else:
                n_components = 6
        else:
            n_components = self.n_components
        
        n_samples, n_features = X.shape
        if self.fitting == "full":
            if n_components > min(n_samples, n_features):
                raise ValueError("n_components should be <= min(n_samples, n_features)")
        elif self.fitting == "lowrank":
            if n_components > min(6, n_samples, n_features):
                raise ValueError("n_components should be <= min(6, n_samples, n_features)")
        
        self.mean_ = torch.mean(X, axis=0)
        X -= self.mean_
        
        if self.fitting == "full":
            U, S, Vt = torch.linalg.svd(X, full_matrices=False)
            # flip eigenvectors' sign to enforce deterministic output
            U, Vt = svd_flip(U, Vt)
        elif self.fitting == "lowrank":
            U, S, Vt = torch.svd_lowrank(X) # n_components = q, default q = min(6, X.shape[0], X.shape[1])
            
        self.components_ = Vt[:n_components]

        self.n_components_ = n_components
        
        return U, S, Vt

    def fit(self, X):
        self._fit(X)
        return self
    
    def transform(self, X):
        assert self.mean_ is not None
        X -= self.mean_

        return torch.matmul(X, self.components_.T)
    
    def fit_transform(self, X):
        U, S, Vt = self._fit(X)
        U = U[:, :self.n_components_]
        U *= S[:self.n_components_]
        return U



class SNP_PCA():
    def __init__(self, backend="sklearn", n_components=None, fitting="full", device='cuda:0'):
        """Class to perform PCA on SNP data using the SNPObject and either sci-kit 
        learn's PCA or a PyTorch PCA implementation.

        Args:
            backend (str, optional): backend. Defaults to "pytorch".
            n_components (int, optional): number of principal components. Defaults to None.
            fitting (str, optional): full or lowrank (only useful for backend="pytorch"). Defaults to "full".
            device (str, optional): device (only useful for backend="pytorch"). Defaults to 'cuda:0'.
        """

        self.n_components = n_components
        self.fitting = fitting
        self.backend = backend
        self.device = device
        self.X = None

        if self.backend == "pytorch":
            self.pca = TorchPCA(n_components=self.n_components, fitting=self.fitting)
        elif self.backend == "sklearn":
            self.pca = PCA(n_components=self.n_components)
        else:
            raise ValueError("Unknown backend for PCA: ", backend)

    def _get_data_from_snpobj(self, snpobj, strands, samples_subset, snps_subset):
        """
        Args:
            snpobj (SNPObject): SNPObject containing the SNPs
            strands (str): "average" to average paternal and maternal strands,
                           or "separate" to create separated maternal and paternal samples.
            samples_subset (int or list): if int: use first n samples, if list: use samples
                                          given by the indexes of the list
            snps_subset (int or list): if int: use first n SNPs, if list: use SNPs
                                       given by the indexes of the list


        Returns:
            np.array or torch.Tensor: SNP data prepared for PCA methods
        """
        X = np.transpose(snpobj.calldata_gt.astype(float), (1,0,2))
        if strands == "average":
            X = np.mean(X, axis=2)
        elif strands == "separate":
            X = np.reshape(X, (-1, X.shape[1]))
        else:
            raise ValueError("Unknown method to deal with paternal and maternal strands: ", strands)
        # TODO: other useful methods to deal with paternal and maternal strands?

        if self.backend == "pytorch":
            X = torch.from_numpy(X).to(self.device)

        if samples_subset is not None:
            if type(samples_subset) == int:
                X = X[:samples_subset]
            elif type(samples_subset) == list:
                X = X[samples_subset, :]
            else:
                raise ValueError("Unknown samples_subset type: ", type(samples_subset))
        
        if snps_subset is not None:
            if type(snps_subset) == int:
                X = X[:, :snps_subset]
            elif type(snps_subset) == list:
                X = X[:, snps_subset]
            else:
                raise ValueError("Unknown samples_subset type: ", type(snps_subset))
        

        return X


    def fit(self, snpobj, strands="average", samples_subset=None, snps_subset=None):
        self.X = self._get_data_from_snpobj(snpobj, strands, samples_subset, snps_subset)
        return self.pca.fit(self.X)
    
    def transform(self, snpobj, strands="average", samples_subset=None, snps_subset=None):
        self.X = self._get_data_from_snpobj(snpobj, strands, samples_subset, snps_subset)
        return self.pca.transform(self.X)
    
    def fit_transform(self, snpobj, strands="average", samples_subset=None, snps_subset=None):
        self.X = self._get_data_from_snpobj(snpobj, strands, samples_subset, snps_subset)
        return self.pca.fit_transform(self.X)


