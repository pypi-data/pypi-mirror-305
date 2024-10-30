.. code:: ipython3

    import os
    import sys
    import numpy as np
    dir = os.path.abspath('../')
    if not dir in sys.path: sys.path.append(dir)
    from snputils.processing import SNP_PCA

.. code:: ipython3

    from snputils.snp.io.read import VCFReader

.. code:: ipython3

    reader = VCFReader("/local-scratch/mrivas/bonet/datasets/genomics/hapmap3/hapmap3.vcf")
    snpobj = reader.read()


.. parsed-literal::

    INFO:snputils.snp.io.read.vcf:Reading .vcf file: /local-scratch/mrivas/bonet/datasets/genomics/hapmap3/hapmap3.vcf
    INFO:snputils.snp.io.read.vcf:Finished reading .vcf file: /local-scratch/mrivas/bonet/datasets/genomics/hapmap3/hapmap3.vcf


 PCA with sklearn backend
=========================

.. code:: ipython3

    snp_pca = SNP_PCA(backend="sklearn", n_components=2)

.. code:: ipython3

    components = snp_pca.fit_transform(snpobj)

.. code:: ipython3

    import pandas as pd
    
    # Create dataframe
    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
    })
    df.head()


.. parsed-literal::

    INFO:numexpr.utils:Note: NumExpr detected 56 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 8.
    INFO:numexpr.utils:NumExpr defaulting to 8 threads.




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Principal Component 1</th>
          <th>Principal Component 2</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>113.696143</td>
          <td>9.880702</td>
        </tr>
        <tr>
          <th>1</th>
          <td>109.031126</td>
          <td>8.175609</td>
        </tr>
        <tr>
          <th>2</th>
          <td>90.237288</td>
          <td>2.417368</td>
        </tr>
        <tr>
          <th>3</th>
          <td>74.617865</td>
          <td>-8.881818</td>
        </tr>
        <tr>
          <th>4</th>
          <td>102.963313</td>
          <td>4.262103</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    import matplotlib.pyplot as plt
    import seaborn as sns

.. code:: ipython3

    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()



.. image:: output_8_0.png


fit() and then transform()
--------------------------

.. code:: ipython3

    snp_pca = SNP_PCA(backend="sklearn", n_components=2)
    snp_pca.fit(snpobj)
    components = snp_pca.transform(snpobj)

.. code:: ipython3

    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()



.. image:: output_11_0.png


separate strands into independent samples
-----------------------------------------

.. code:: ipython3

    snp_pca = SNP_PCA(backend="sklearn", n_components=2)
    components = snp_pca.fit_transform(snpobj, strands="separate")
    print(components.shape)
    
    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()


.. parsed-literal::

    (2368, 2)
    WARNING:matplotlib.legend:No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.



.. image:: output_13_1.png


subset of samples
-----------------

.. code:: ipython3

    snp_pca = SNP_PCA(backend="sklearn", n_components=2)
    components = snp_pca.fit_transform(snpobj, samples_subset=100)
    print(components.shape)
    
    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()


.. parsed-literal::

    (100, 2)



.. image:: output_15_1.png


.. code:: ipython3

    snp_pca = SNP_PCA(backend="sklearn", n_components=2)
    components = snp_pca.fit_transform(snpobj, samples_subset=[0,1,2,3,99,1004,1067])
    print(components.shape)
    
    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()


.. parsed-literal::

    (7, 2)



.. image:: output_16_1.png


subset of snps
==============

.. code:: ipython3

    snp_pca = SNP_PCA(backend="sklearn", n_components=2)
    components = snp_pca.fit_transform(snpobj, snps_subset=500)
    print(components.shape)
    
    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()


.. parsed-literal::

    (1184, 2)



.. image:: output_18_1.png


.. code:: ipython3

    snp_pca = SNP_PCA(backend="sklearn", n_components=2)
    components = snp_pca.fit_transform(snpobj, snps_subset=[0,1,2,3,99,1004,1067])
    print(components.shape)
    
    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()


.. parsed-literal::

    (1184, 2)



.. image:: output_19_1.png


subset of samples and subset of snps
====================================

.. code:: ipython3

    snp_pca = SNP_PCA(backend="sklearn", n_components=2)
    components = snp_pca.fit_transform(snpobj, snps_subset=500, samples_subset=50)
    print(components.shape)
    
    df = pd.DataFrame({
        "Principal Component 1": components[:,0],
        "Principal Component 2": components[:,1],
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()


.. parsed-literal::

    (50, 2)



.. image:: output_21_1.png


TorchPCA with SNP\_PCA
======================

be careful with GPU memory --> use subsets of samples or SNPs when doing
the fit() / fit\_transform() if CUDA out of memory

fit() and then transform()
--------------------------

.. code:: ipython3

    snp_pca = SNP_PCA(backend="pytorch", n_components=2)
    snp_pca.fit(snpobj, samples_subset=100)
    components = snp_pca.transform(snpobj, samples_subset=100)

.. code:: ipython3

    components.shape




.. parsed-literal::

    torch.Size([100, 2])



.. code:: ipython3

    import pandas as pd
    df = pd.DataFrame({
        "Principal Component 1": components[:,0].cpu(),
        "Principal Component 2": components[:,1].cpu(),
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()



.. image:: output_26_0.png


 Lowrank
--------

.. code:: ipython3

    snp_pca = SNP_PCA(backend="pytorch", n_components=2, fitting="lowrank")
    snp_pca.fit(snpobj)
    components = snp_pca.transform(snpobj, samples_subset=100)


::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_907260/3431525214.py in <module>
          1 snp_pca = SNP_PCA(backend="pytorch", n_components=400, fitting="lowrank")
    ----> 2 snp_pca.fit(snpobj)
          3 components = snp_pca.transform(snpobj, samples_subset=100)


    ~/git/snputils/snputils/processing/pca.py in fit(self, snpobj, strands, samples_subset, snps_subset)
        163     def fit(self, snpobj, strands="average", samples_subset=None, snps_subset=None):
        164         self.X = self._get_data_from_snpobj(snpobj, strands, samples_subset, snps_subset)
    --> 165         return self.pca.fit(self.X)
        166 
        167     def transform(self, snpobj, strands="average", samples_subset=None, snps_subset=None):


    ~/git/snputils/snputils/processing/pca.py in fit(self, X)
         72 
         73     def fit(self, X):
    ---> 74         self._fit(X)
         75         return self
         76 


    ~/git/snputils/snputils/processing/pca.py in _fit(self, X)
         53         elif self.fitting == "lowrank":
         54             if n_components > min(6, n_samples, n_features):
    ---> 55                 raise ValueError("n_components should be <= min(6, n_samples, n_features)")
         56 
         57         self.mean_ = torch.mean(X, axis=0)


    ValueError: n_components should be <= min(6, n_samples, n_features)


separate strands into independent samples
-----------------------------------------

.. code:: ipython3

    snp_pca = SNP_PCA(backend="pytorch", n_components=2)
    components = snp_pca.fit_transform(snpobj, strands="separate", snps_subset=200)
    print(components.shape)
    
    df = pd.DataFrame({
        "Principal Component 1": components[:,0].cpu(),
        "Principal Component 2": components[:,1].cpu(),
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()


.. parsed-literal::

    torch.Size([2368, 2])



.. image:: output_30_1.png


subset of samples and subset of snps
====================================

.. code:: ipython3

    snp_pca = SNP_PCA(backend="pytorch", n_components=2)
    components = snp_pca.fit_transform(snpobj, snps_subset=500, samples_subset=50)
    print(components.shape)
    
    df = pd.DataFrame({
        "Principal Component 1": components[:,0].cpu(),
        "Principal Component 2": components[:,1].cpu(),
    })
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x="Principal Component 1", y="Principal Component 2", linewidth=0, alpha=0.5)
    plt.grid()
    plt.xlabel("Principal Component 1", fontsize=20)
    plt.ylabel("Principal Component 2", fontsize=20)
    plt.title("PCA on Hapmap3", fontsize=30)
    plt.tight_layout()
    plt.show()


.. parsed-literal::

    torch.Size([50, 2])



.. image:: output_32_1.png

