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
