# Installation

[安装过程的视频讲解](https://www.bilibili.com/video/BV1BH4y1J7m2/)

DuIvyProcedures(DIP)有诸多依赖，比较建议先通过conda或者mamba、或自行设置好环境以及相关的依赖。

## conda环境设置

创建conda环境：

```bash
conda create -n DIP python=3.9
```

**请注意，目前DIP仅支持python3.9版本，如果有其他版本需求，请联系杜艾维**

激活conda环境：

```bash
conda activate DIP
```

安装如下的依赖：

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

首先通过conda安装rdkit：

```bash
conda install -c conda-forge rdkit
```

然后安装其他依赖：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple WMI psutil pycryptodome PyYAML numpy pandas matplotlib MDAnalysis DuIvyTools scikit-learn scipy seaborn igraph deeptime umap-learn pycairo colorama
```

## GROMACS设置

如果用户需要使用依赖于GROMACS的分析模块，用户需要保证GROMACS2019及以上版本已经正确安装并可以通过命令行调用。

DIP支持`gmx`、`gmx_mpi`等多种调用的软件名，只需要在任务输入的yaml文件中写明即可。但用户需要保证安装的GROMACS版本具有`cluster`、`rms`、`rmsf`、`sasa`等常见的分析命令。

其中，`gmx do_dssp`命令在GROMACS版本低于2023的时候，需要依赖于DSSP软件才可以运行，请参照https://zhuanlan.zhihu.com/p/380242442进行设置。

## Linux设置

如果用户使用的是Linux操作系统，请保证当前用户可以**以普通用户权限运行`dmidecode`命令**。

一般的权限设置过程如下：

首先找到`dmidecode`命令的路径，例如：

```bash
which dmidecode
```

或者：

```bash
where dmidecode
```

假设路径为：

```bash
/usr/sbin/dmidecode
```

通过下列命令赋予普通用户调用`dmidecode`命令的权限：

```bash
sudo chmod +s /usr/sbin/dmidecode
```

这样，普通用户就可以以普通用户权限运行`dmidecode`命令了。例如：

```bash
$ dmidecode -s processor-manufacturer
Intel(R) Corporation
```



## DIP安装

【杜艾维】公众号后台联系杜若获取DIP安装包。之后使用conda环境中的pip命令正常安装即可：

```bash
pip install DuIvyProcedures-xxxx--py3-none-any.whl
```

安装完成之后，在命令行中运行`dip`命令查看输出：

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


DuIvyProcedures(DIP, ©杜艾维): To ease your MD analysis. 
Available analysis modules: gmx_RMSD, gmx_Gyrate, gmx_RMSF, gmx_SASA, gmx_DCCM, gmx_DSSP, gmx_Cluster, gmx_Mdmat, gmx_PCA, gmx_FEL, gmx_dPCA, gmx_Hbond, gmx_Density, Density, RMSD, RMSF, Gyrate, RDF, tICA, tSNE, PCA, UMAP, SPM, DCCM, RDCM, SaltBridge, PiStacking, DensityMap, User_Mod
```

此时DIP已经成功安装，但是还不能运行分析，需要获取使用授权。
1. 运行`dip code`命令生成DIP识别码，也即DIP会在当前目录生成DIP_code_file文件
2. 向杜艾维提供DIP_code_file文件，购买使用授权并获得授权文件DIP_license_file
3. 在DIP_license_file的保存目录执行`dip code -f DIP_license_file`命令激活授权
4. 再次运行`dip code`检查授权状态

至此安装完成，建议用户先跑一下测试案例，确认运行正常。

## DIP测试

访问[测试案例](http://charles8hahn.pythonanywhere.com/download/DIP_test.zip)下载测试轨迹文件，解压后在DIP_test文件夹路径下运行`dip run -f dip_test.yaml`命令，默认的测试将进行，大约会在约60分钟后结束（取决于电脑性能，i7-6700H芯片上测的60分钟）。

如果一切顺利，运行成功，会在当前目录生成各种分析的文件夹，里面包含了运行结果，可以自行查看。

如果不想跑完全部的分析，也可以在dip_test.yaml文件中用`#`注释掉不需要的分析手段。

如果OK，则DIP可用了。祝您科研愉快~

如果有任何问题，请联系杜若。



