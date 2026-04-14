# Installation

[Video Tutorial for Installation](https://www.bilibili.com/video/BV1BH4y1J7m2/)

DuIvyProcedures (DIP) has many dependencies. It is recommended to set up the environment and related dependencies through conda or mamba first, or set them up manually.

## conda Environment Setup

Create a conda environment:

```bash
conda create -n DIP python=3.9
```

**Note: Currently DIP only supports Python 3.9. If you need other versions, please contact Du Ivy**

Activate the conda environment:

```bash
conda activate DIP
```

DIP has the following dependencies:

```txt
colorama           0.4.6
WMI                1.5.1
psutil             5.9.8
pycryptodome       3.20.0
PyYAML             6.0.1

numpy              1.26.4
pandas             2.1.4
matplotlib         3.8.3
MDAnalysis         2.7.0
DuIvyTools         0.5.3

rdkit                     # PiStacking only if byIndex==no
scikit-learn       1.4.1  # PCA 
scipy              1.12.0 # RDCM
seaborn            0.13.2 # saltbridge
igraph             0.11.4 # SPM
pycairo            1.26.0 # SPM
deeptime           0.4.4  # tICA
umap-learn         0.5.5  # umap
```

All dependencies including rdkit can be installed via pip:

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple rdkit WMI psutil pycryptodome PyYAML numpy pandas matplotlib MDAnalysis DuIvyTools scikit-learn scipy seaborn igraph deeptime umap-learn pycairo colorama
```

## GROMACS Setup

If users need to use analysis modules that depend on GROMACS, users need to ensure that GROMACS 2019 or higher is properly installed and can be called from the command line.

DIP supports various software names like `gmx`, `gmx_mpi`, etc. Users only need to specify them in the task input yaml file. However, users need to ensure that the installed GROMACS version has common analysis commands such as `cluster`, `rms`, `rmsf`, `sasa`, etc.

Note that `gmx do_dssp` command in GROMACS versions below 2023 requires DSSP software to run. Please refer to https://zhuanlan.zhihu.com/p/380242442 for setup instructions.

## Linux Setup

If you are using a Linux operating system, please ensure that the current user can **run the `dmidecode` command with regular user privileges**.

The general permission setup process is as follows:

First, find the path to the `dmidecode` command, for example:

```bash
which dmidecode
```

Or:

```bash
where dmidecode
```

Assume the path is:

```bash
/usr/sbin/dmidecode
```

Grant regular users permission to call the `dmidecode` command with the following command:

```bash
sudo chmod +s /usr/sbin/dmidecode
```

Now, regular users can run the `dmidecode` command with regular user privileges. For example:

```bash
$ dmidecode -s processor-manufacturer
Intel(R) Corporation
```



## DIP Installation

Contact Du Ruo through the [杜艾维] WeChat Official Account backend to obtain the DIP installation package. Then use the pip command in the conda environment to install normally:

```bash
pip install DuIvyProcedures-xxxx--py3-none-any.whl
```

After installation is complete, run the `dip` command in the command line to view the output:

```bash
(DIP) $ dip

[Info] 2024-02-23 14:14:33


 /$$$$$$$           /$$$$$$                          /$$$$$$$ 
| $$__  $$         |_  $$_/                         | $$__  $$
| $$  \ $$ /$$   /$$ | $$ /$$    /$$ /$$   /$$      | $$  \ $$
| $$  | $$| $$  | $$ | $$|  $$  /$$/| $$  | $$      | $$$$$$$/
| $$  | $$| $$  | $$ | $$ \  $$/$$/ | $$  | $$      | $$____/ 
| $$  | $$| $$  | $$ | $$  \  $$$/  | $$  | $$      | $$      
| $$$$$$$/|  $$$$$$//$$$$$$ \  $/   |  $$$$$$$      | $$      rocedures
|_______/  \______/|______/  \_/     \____  $$      |__/      
                                     /$$  | $$                
                                    |  $$$$$$/                
                                     \______/                 


DuIvyProcedures(DIP, ©Du Ivy): To ease your MD analysis. 
Available analysis modules: gmx_RMSD, gmx_Gyrate, gmx_RMSF, gmx_SASA, gmx_DCCM, gmx_DSSP, gmx_Cluster, gmx_Mdmat, gmx_PCA, gmx_FEL, gmx_dPCA, gmx_Hbond, gmx_Density, Density, RMSD, RMSF, Gyrate, RDF, tICA, tSNE, PCA, UMAP, SPM, DCCM, RDCM, SaltBridge, PiStacking, DensityMap, User_Mod
```

At this point, DIP has been successfully installed, but analysis cannot be run yet. You need to obtain a usage license.
1. Run the `dip code` command to generate a DIP identification code, i.e., DIP will generate a DIP_code_file file in the current directory
2. Provide the DIP_code_file file to Du Ivy, purchase a usage license and obtain the license file DIP_license_file
3. Execute the `dip code -f DIP_license_file` command in the directory where DIP_license_file is saved to activate the license
4. Run `dip code` again to check the license status

Installation is now complete. It is recommended that users run the test case first to confirm normal operation.

## DIP Testing

Visit [Test Case](http://charles8hahn.pythonanywhere.com/download/DIP_test.zip) to download the test trajectory files. After extraction, run the `dip run -f dip_test.yaml` command in the DIP_test folder path. The default test will run and complete in approximately 60 minutes (depending on computer performance, 60 minutes measured on an i7-6700H chip).

If everything goes smoothly and runs successfully, analysis folders will be generated in the current directory containing the results, which you can view yourself.

If you don't want to run all analyses, you can also comment out unnecessary analysis methods with `#` in the dip_test.yaml file.

If OK, then DIP is ready to use. Enjoy your research~

If you have any questions, please contact Du Ruo.