# gmx_PCA

本模块依赖GROMACS进行所选原子组的坐标的主成分分析。

使用本模块前请注意[前置处理](https://duivyprocedures-docs.readthedocs.io/en/latest/Framework.html#id7)已经完成！

## Input YAML

```yaml
- gmx_PCA:
    group: C-alpha
    gmx_parm:
      tu: ns
```

`group`: 选择要进行主成分分析的原子组，对于蛋白质一般可以选择C-alpha。

`gmx_parm`: 用户可以在这里附加一些`gmx covar`和`gmx anaeig`命令的共有的参数，例如控制时间的`-b -e`等。

## Output

完成PCA计算之后，本模块会导出前三个主成分并分别绘制两两主成分的散点图，以及所有和前10主成分的占比折线图。

![gmx_PCA_dpc12](static/gmx_PCA_pc12_scatter.png)

![gmx_PCA_dpc13](static/gmx_PCA_pc13_scatter.png)

![gmx_PCA_dpc23](static/gmx_PCA_pc23_scatter.png)

![gmx_PCA_10](static/gmx_PCA_eigenval_probability_first_10.png)

![gmx_PCA_all](static/gmx_PCA_eigenval_probability.png)

同时DIP也会整理好前三个主成分的两两主成分的xvg文件，可以直接用于`gmx_FEL`模块绘制基于PCA的自由能形貌图。

主成分余弦含量(cosine content)的计算也是对PCA的一种检查。DIP会计算每个PC的余弦含量并输出。当前几个成分的余弦含量的值接近1时，说明该PC可能对应于随机扩散，也即意味着模拟没有收敛，采样较差。关于更多余弦含量的内容，请参考 Berk Hess. Convergence of sampling in protein simulations. Phys. Rev. E 65, 031910 (2002).

前三个主成分的极值在轨迹上的投影也会输出到pdb文件，如`pc1_proj.pdb`，可以通过pymol等工具可视化查看沿PC方向结构的变化。

## References

如果您使用了DIP的本分析模块，请一定引用GROMACS模拟引擎、DuIvyTools(https://zenodo.org/doi/10.5281/zenodo.6339993)，以及合理引用本文档(https://zenodo.org/doi/10.5281/zenodo.10646113)。