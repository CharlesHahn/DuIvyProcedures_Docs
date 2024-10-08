# FrameWork 

DIP由几个部分组成：分析模块、控制模块、输入控制模块。

## 分析模块

分析模块主要是执行分析的模块，包含了执行各种分析以及产生分析结果的代码。


## 控制模块

控制模块包含了串行执行各种分析、路径控制、参数控制、日志记录等功能。

## 输入控制模块

DIP使用YAML格式的文件来存储用户输入的分析模块的参数信息。该文件中包含了GROMACS路径、轨迹文件、拓扑文件，需要执行分析的路径，以及需要执行的分析任务的名字及相关参数等情况。

**请注意！DIP不会对用户的轨迹进行周期性矫正，请用户先自行校正轨迹，保证分子完整性、相互之间位置的合理性！**

### 参数文件的产生

用户可以通过如下命令产生一个包含了全部分析模块的参数文件：

```bash
dip conf -o dip.yaml
```

或者可以通过`-t`或者`-d`命令指定要进行的分析手段或者待分析的路径：

```bash
dip conf -o dip.yaml -t gmx_RMSD DCCM -d MD0
```

### 参数文件的修改

一般来说，默认生成的参数文件**不是开箱可用的**。需要用户根据实际情况进行修改。

常见的需要修改的地方包括：gmx可执行程序的路径、轨迹文件和拓扑文件的名字、执行分析的路径（该路径下必须包含设置的轨迹文件和拓扑文件）、以及各种分析模块的输入参数等。

请参照下方输入参数yaml文件解析，以及对应分析模块的输入参数部分。


### 参数文件的使用

要执行分析，请运行：

```bash
dip run -f dip.yaml
```

DIP会按照分析路径和分析模块的顺序，依次执行分析任务，并将结果保存在对应的分析目录下。

### 用户输入的yaml文件内容解析


用于用户输入的YAML文件至少需要包含以下三个部分：

```yaml
Path:
 - MD0
 - MD1
 - MD2

Conf:
  gmx: gmx
  xtc: md.xtc
  tpr: md.tpr
  ndx: index.ndx

Tasks:
  - gmx_RMSD:
      fit_group: Backbone
      calc_group: Protein
      rmsd_matrix: no
      gmx_parm:
        tu: ns
```

Path部分用于指定分析的路径，可以指定多个路径；DIP会依次对每个路径下的轨迹进行分析；

Conf部分用于配置GROMACS的路径、输入文件名、索引文件名等信息；不同分析路径下的这些文件需要名字一致。例如两个不同的模拟体系，MD0和MD1，在其目录下的轨迹文件的名字都需要是md.xtc，才能被DIP读取和分析。

对于不依赖GROMACS的分析任务（分析模块不以`gmx_`开头），轨迹文件和拓扑文件等可以是其它的格式，比如amber格式的轨迹和拓扑文件，DIP同样能识别。

Conf部分自v1.0.3开始还能添加一个控制输出图片格式的参数`fig`，默认情况下输出的图片为png格式，可以将`fig`参数设置为`pdf`、`svg`等格式，即可输出多种格式的图片。例如：

```yaml
Conf:
  gmx: gmx
  xtc: md.xtc
  tpr: md.tpr
  ndx: index.ndx
  fig: pdf
```

Tasks部分用于指定具体的分析任务，每个任务都有自己的参数，具体的分析任务由分析模块的具体实现决定。

Tasks部分的第一行是分析模块的名字，再下面是隶属于该分析模块的参数。例如这里的gmx_RMSD模块下面需要设定fit_group等参数。

这里的gmx_parm参数下面可以写入该分析模块所依赖的gmx命令的相关参数。例如gmx rmsd命令可以有`-b -e -tu`等参数，那么在这里可以设置为:

```yaml
gmx_parm:
  b: 0
  e: 10000
  tu: ns
```

DIP会直接将用户设置的gmx_parm下面的参数连接到gmx命令中进行执行。当然，`gmx_parm`参数不是必须的，如果您不需要添加额外的参数的话。

每一个分析模块下面都有一个隐藏参数：`mkdir`。如果我们同时执行两个不同参数的同种分析，则需要将分析结果放置在不同的文件夹中，因而`mkdir`参数可以指定一个文件夹名，将该分析结果放置在该文件夹下，默认情况下，`mkdir`的参数就是该分析模块的名字。

```yaml
Tasks:
  - gmx_RMSD:
      fit_group: Backbone
      calc_group: Protein
      rmsd_matrix: no
      gmx_parm:
        tu: ns
  - gmx_RMSD:
      mkdir: gmx_RMSD2
      fit_group: Protein
      calc_group: Protein
      rmsd_matrix: yes
```

所有依赖GROMACS的分析模块，其中的选组参数的值，都必须是模拟体系中自然有的分组，如`System`、`Protein`、`Backbone`等、或者是用户通过GROMACS索引文件定义的组。

**请注意，所有组的名字都必须以英文开头，不要有空格，不能以数字开头！** 数字开头的组，如`6Lig`会被GROMACS识别成第6个组而不是6Lig组。

所有不依赖GROMACS的分析模块（不以`gmx_`开头）还有三个隐藏参数可以对轨迹做帧的选择：

```yaml
      frame_start:  # start frame index
      frame_end:   # end frame index, leave blank for all frames
      frame_step:  # frame index step, default=1
```

这些参数可以指定计算轨迹的起始帧、终止帧（不包含）以及帧的步长。默认情况下，用户不需要设置这些参数，模块会自动分析整个轨迹。

例如我们计算从1000帧开始，到5000帧结束，每隔10帧的数据：

```yaml
      frame_start: 1000 # start frame index
      frame_end:  5001 # end frame index, None for all frames
      frame_step: 10 # frame index step, default=1
```

如果三个参数中只需要设置一个或两个，其余的参数都可以省略。

其他的分析模块的参数也类似，具体的分析模块的参数请参考具体的分析模块的文档。


## 前置处理

有一些处理需要用户在使用DIP运行分析之前自行操作。

1. 如果用户使用基于gmx的组件，则需要自行准备好拓扑文件和轨迹文件、以及索引文件。请注意，轨迹文件需要**自行进行周期性矫正**，保证分子完整性、相互之间位置的合理性。同时索引文件里面的分组以及名字都需要自行生成。

2. 如果用户使用基于MDAnalysis的组件，则需要自行准备好拓扑文件和轨迹文件。请注意，轨迹文件需要**自行进行周期性矫正**，保证分子完整性、相互之间位置的合理性。**拓扑文件和轨迹文件里面的原子数目必须一一对应上**，不然MDAnalysis无法读取。

3. 由于GROMACS2024在诸多分析命令上有改变，所以DIP中依赖GROMACS的分析模块可能不适用于GROMACS2024，建议是GROMACS2019到2023版本。另外如果是GROMACS2022及以下版本，运行DIP的`gmx_DSSP`组件依赖于`gmx do_dssp`命令，因而请用户自行确保DSSP已经正确安装且`gmx do_dssp`命令可用。运行`PiStacking`组件时，如果需要DIP自动寻找可能的芳香环，请确保rdkit已经正确安装并可调用。
