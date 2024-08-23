# 常见问题及说明

### 1. rdkit安装问题

网上常见的rdkit安装方法一般是通过conda安装，现在笔者更推荐直接使用pip安装，对于windows和linux都有很好的pip包，比conda安装更方便更快捷，更不容易遇到编译问题。

这里我们使用pip安装，同时调用清华源，安装更加快捷：

```bash
pip install rdkit -i https://pypi.tuna.tsinghua.edu.cn/simple
```

关于rdkit的pip包，可以查看：https://pypi.org/project/rdkit-pypi

安装完成之后，打开python的命令行，输入如下两行代码验证rdkit安装是否成功：

```python
from rdkit import Chem
print(Chem.MolToMolBlock(Chem.MolFromSmiles('C1CCC1')))
```

如果没有报错，一般可以说明安装成功。


### 2. windows的cmd运行DIP命令出现编码问题

Linux系统一般使用的都是utf-8编码，极少出现编码问题。
而国内Windows系统常见的有两种编码方式，一种是utf-8，一种是gbk。这就有可能导致DIP在执行系统命令的过程中出现编码问题。

例如在cmd中运行DIP可能会遇到如下的编码报错：

```bash
UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 11: illegal multibyte sequence
```

遇到这种编码问题，一般可以尝试如下的解决方案：

首先检查cmd的编码：

```bash
chcp
```

如果输出是65001，则说明cmd的编码是utf-8。否则我们可能需要更改一下cmd的编码：

```bash
chcp 65001
```

在cmd中运行这条命令能够将cmd的编码临时转换为utf-8。

同时，建议设置一下python编码的环境变量：

```bash
set PYTHONUTF8=1
```

当然也可以在windows系统的环境变量中设置如上的环境变量，变量名为PYTHONUTF8，值为1。

这样在运行python脚本的时候，默认的编码就为utf-8。

以上两个操作基本上可以保证cmd中运行DIP命令不会出现编码问题。


### 3. 如何更改输出图片的默认样式？

大多数情况下DIP都是调用环境中的DIT进行绘图，某些情况下是使用DIP自身的绘图功能进行绘图，因而可以通过调整环境中的DIT的matplotlib样式控制以及DIP的样式控制来更改输出图片的样式。

以下说明环境中DIT的默认样式控制文件以及DIP的样式控制文件的位置：

环境中DIT的默认样式控制文件：

```bash
conda_install_location/envs/DIP/Lib/site-packages/DuIvyTools/DuIvyTools/data/mplstyle/DIT.mplstyle
```

环境中DIP的默认样式控制文件：

```bash
conda_install_location/envs/DIP/Lib/site-packages/DuIvyProcedures/data/DIP.mplstyle
```

用户可以通过调整样式控制文件的内容来调控出图的样式，例如调整字体大小、颜色循环等等：

```txt
## Matplotlib style for DuIvyTools
## https://matplotlib.org/stable/tutorials/introductory/customizing.html#the-matplotlibrc-file

axes.labelsize:     16
axes.linewidth:     1
xtick.labelsize:    16
ytick.labelsize:    16
ytick.left:         True
ytick.direction:    in
xtick.bottom:       True
xtick.direction:    in
lines.linewidth:    2
legend.fontsize:    14
legend.loc:         best
legend.fancybox:    False
legend.frameon:     False
font.family:        Arial
font.size:          16
image.cmap:         coolwarm
image.aspect:       auto # for fitting into axes
# figure.figsize:     6, 5
figure.dpi:         100
savefig.dpi:        300
axes.prop_cycle:    cycler('color', ['38A7D0', 'F67088', '66C2A5', 'FC8D62', '8DA0CB', 'E78AC3', 'A6D854', 'FFD92F', 'E5C494', 'B3B3B3', '66C2A5', 'FC8D62'])
```


### 4. 如何查看分析模块调用的系统命令？

在分析过程中，DIP会调用DIT以及一些系统命令去执行分析和可视化，有时候我们也需要对可视化结果进行调优，调整一些参数等等，那我们要如何查看DIP用到的这些命令呢？

DIP的每一个分析模块都会在成功运行之后输出一个log文件，这个log文件中记录了用到的所有命令，包括gmx命令和DIT的命令，例如：

```bash
[Info] 2024-08-17 17:44:25
>>> run gmx_RMSD module in C:\Users\hhhhh\Desktop\DuIvyProcedures\test\DIP_test\MD
[Info] 2024-08-17 17:44:27
Pid 15264 >>> echo Backbone Protein | gmx rms -s ../md.tpr -f ../md.xtc -n ../index.ndx -o rmsd_Protein2Backbone.xvg -m rmsd_matrix_Protein2Backbone.xpm -tu ns  -dt 1 
[Info] 2024-08-17 17:44:28
Pid 16560 >>> dit xvg_compare -f rmsd_Protein2Backbone.xvg -c 1 -l "" -t "" -ns -o RMSD_Protein2Backbone.png
[Info] 2024-08-17 17:44:31
Pid 6580 >>> dit xpm_show -f rmsd_matrix_Protein2Backbone.xpm -cmap coolwarm -o RMSD_matrix_Protein2Backbone.png -ns


>>>>>> run terminal command log <<<<<<
[Info] 2024-08-17 17:44:27
......
```

这是gmx_RMSD模块log文件的一部分，可以看到前头的部分内容即是DIP调用`gmx rms`命令去执行RMSD分析，后面两条命令则是调用DIT的`xvg_compare`和`xpm_show`命令进行可视化。

在`command log`部分现实的记录的则是命令执行的回显和相关的信息，一般可以用于检查报错信息等。

用户可以根据这些信息，自行加以调整以优化可视化效果或者检查数据正确性等。



# 开发计划与日志

## 开发计划

### 1.0版本

后续还会继续优化和升级已有组件，并添加基础分析相关的模块。

用户有任何建议，或者发现了任何问题，请在微信群公告里的反馈链接中填写相关信息。杜艾维会尽量及时回复并跟进。因为时间有限，开发任务进展会较为缓慢，修bug可能会快一些。

后续的版本升级请关注群消息和本页面的开发日志。


### 1.1版本

1.1大版本最早将于2025年发布，主要可能会增加更多非共价分析模块、膜相关的分析模块、以及可能的部分材料相关的分析模块；在主体框架上，会改进日志系统、增加模块并行计算的功能。

开发任务：
- [ ] 更多相互作用的分析模块
- [ ] 膜相关分析
- [ ] 模块并行计算
  

## 开发日志

2024.02.04 完成框架、分析模块的开发、完成文档撰写

2024.02.26 完成多轮测试和优化，正式发布1.0版本

2024.03.24 添加FEL、Hbond、PiCation、Hydrophobic、MSM等新组件，对已有组件添加了新功能，修复已知问题；DIP的v1.0版本基本功能完善结束；发布v1.0.2版本
