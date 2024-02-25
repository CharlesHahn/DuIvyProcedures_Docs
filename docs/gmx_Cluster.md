# gmx_cluster

gmx_Cluster模块依赖`gmx cluster`命令对轨迹进行聚类分析，并针对`gmx cluster`命令的输出结果进行解析，生成可视化结果，包括可视化RMSD矩阵、聚类大小、聚类分布等情况。

使用本模块前请注意[前置处理](https://duivyprocedures-docs.readthedocs.io/en/latest/Framework.html#id7)已经完成！

## Input YAML

```yaml
  - gmx_Cluster:
      fit_group: Backbone
      calc_group: Protein
      gmx_parm:
        method: gromos
        cutoff: 0.1
        tu: ns
        dt: 0.1
```

`fit_group`：聚类分析首先需要对轨迹进行对齐，此选项为对齐组，默认为`Backbone`。

`calc_group`：需要进行聚类分析的计算组，默认为`Protein`。

`gmx_parm`：`gmx cluster`命令的参数设置，包括`method`、`cutoff`、`tu`、`dt`等等。`gmx cluster`命令可用的参数，都可以在这里进行设置。有几个参数是DIP默认添加了的，所以不需要用户在yaml文件中声明：`-o`、`-g`、`-sz`、`-cl`以及`-clndx`。轨迹文件、tpr文件、ndx文件都是通过yaml的Conf部分进行输入的，因而这里也不需要输入了。

请注意，`gmx cluster`的时间步长，也即`dt`设置得较短的话，会导致有较多的帧需要分析，计算量较大，耗时会较长，同时输出的pdb文件也会很大；请用户根据自身需要设置相应的参数。

## Output

执行此模块之后，DIP会自动调用`gmx cluster`命令并执行聚类，之后DIP会对rmsd-clust.xpm、clust-size.xvg、以及rmsd-dist.xvg进行绘图。
所有的结果文件、可视化图片、每一个类的占比数据和折线图，以及DIP的log文件都可以在分析路径下的相关文件夹里找到。

## References

如果您使用了DIP的本分析模块，请一定引用GROMACS模拟引擎、DuIvyTools(https://zenodo.org/doi/10.5281/zenodo.6339993)，以及合理引用本文档(https://zenodo.org/doi/10.5281/zenodo.10646113)。

