# Installation

DuIvyProcedures(DIP)有诸多依赖，比较建议先通过conda或者mamba、或自行设置好环境以及相关的依赖。

## conda环境设置

创建conda环境：

```bash
conda create -n DIP python=3.8
```

**请注意，目前DIP仅测试了python3.8版本。建议安装python=3.8**

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

numpy              1.23.1
pandas             2.0.3
matplotlib         3.5.3
MDAnalysis         2.4.3
DuIvyTools         0.5.3

rdkit                     # PiStacking only if byIndex==no
scikit-learn       1.3.2  # PCA 
scipy              1.10.1 # RDCM
seaborn            0.13.2 # saltbridge
igraph             0.11.3 # SPM
pycairo            1.25.1 # SPM
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

用户需要保证GROMACS2019及以上版本已经正确安装并可以通过命令行调用。

DIP支持`gmx`、`gmx_mpi`等多种调用的软件名，只需要在任务输入的yaml文件中写明即可。但用户需要保证安装的GROMACS版本具有`cluster`、`rms`、`rmsf`、`sasa`等常见的分析命令。

## DIP安装

【杜艾维】公众号后台联系杜若获取DIP安装包。之后使用conda环境中的pip命令正常安装即可：

```bash
pip install DuIvyProcedures-xxxx--py3-none-any.whl
```

安装完成之后，在命令行中运行`dip`命令查看输出：

```bash
(DIP) $ dip

here is dip's output...
```

此时DIP已经成功安装，但是还不能运行分析，需要获取使用授权。
1. 运行`dip code`命令生成DIP识别码，也即DIP会在当前目录生成DIP_code_file文件
2. 向杜艾维提供DIP_code_file文件，购买使用授权并获得授权文件DIP_license_file
3. 在DIP_license_file的保存目录执行`dip code -f DIP_license_file`命令激活授权
4. 再次运行`dip code`检查授权状态

至此安装完成，建议用户先跑一下测试案例，确认运行正常。

## DIP测试

访问[测试案例](http://charles8hahn.pythonanywhere.com/download/DIP_test.zip)下载测试轨迹文件，解压后在DIP_test文件夹路径下运行`dip run -f dip_test.yaml`命令，默认的测试将进行，大约会在约60分钟后结束（取决于电脑性能，i7-6700H芯片上测的60分钟）。

如果一切顺利，运行成功，会在当前目录生成各种分析的文件夹，里面包含了运行结果，可以自行查看。如果不想跑完全部的分析，也可以在dip_test.yaml文件中用`#`注释掉不需要的分析手段。

如果OK，则DIP可用了。祝您科研愉快~

如果有任何问题，请联系杜若。



