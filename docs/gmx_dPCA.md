# gmx_dPCA

本模块利用GROMACS进行蛋白质骨架二面角的主成分分析。

具体计算过程请参考：https://zhuanlan.zhihu.com/p/479009558

由于`gmx angle`命令的存在，此模块的计算会非常慢；同时考虑到DIP不限制GROMACS的版本，而有些GROMACS版本中`gmx anaeig`命令的输出可能存在问题；再加上dPCA计算还有些科学性上的争议：
- https://doi.org/10.1002/prot.20310
- https://doi.org/10.1063/1.2746330

因此，**建议用户使用此模块进行dPCA计算之后仔细检查分析结果！！！**

使用本模块前请注意[前置处理](https://duivyprocedures-docs.readthedocs.io/en/latest/Framework.html#id7)已经完成！

## Input YAML

```yaml
- gmx_dPCA:
    group: Protein
    fast_mode: no
    gmx_parm:
      tu: ns
```

`group`：蛋白质组名，即`Protein`，也可以选择包含了骨架原子的其他组。
`gmx_parm`：此模块涉及到多个GROMACS命令，这里的gmx_parm参数只会被添加到`gmx anaeig`命令中，用于导出主成分，因而可以一般可以用户自定义`gmx anaeig`命令的参数。

`fast_mode`：是否使用快速模式。在执行dPCA分析的过程中，有一步`gmx angle`生成二面角的trr文件的步骤，因为该命令在生成了trr文件之后会执行一些统计计算的工作，所以需要等待非常长的时间。如果用户设置了`fast_mode: yes`，DIP不会等待`gmx angle`命令执行完，在dangle.trr文件生成之后，DIP会kill掉`gmx angle`进程，并继续执行后续的计算。**请注意，在windows系统上，可能由于各种原因导致`gmx angle`命令无法kill掉，但不影响DIP的计算。用户可以手动kill掉`gmx angle`进程。**

**请注意，因为此分析方法依赖于GROMACS，且有一些dirty tricks，所以不能保证一定能执行完成。** 例如，用于储存二面角的trr文件中如果某一个“原子”的三个坐标值都是0的话，GROMACS会报错，导致程序无法继续执行。


## Output

完成dPCA计算之后，本模块会导出前三个主成分并分别绘制两两主成分的散点图，以及所有和前10主成分的占比折线图。

![gmx_dPCA_dpc12](static/gmx_dPCA_dpc12_scatter.png)

![gmx_dPCA_dpc13](static/gmx_dPCA_dpc13_scatter.png)

![gmx_dPCA_dpc23](static/gmx_dPCA_dpc23_scatter.png)

![gmx_dPCA_10](static/gmx_dPCA_eigenval_probability_first_10.png)

![gmx_dPCA_all](static/gmx_dPCA_eigenval_probability.png)

同时DIP也会整理好前三个主成分的两两主成分的xvg文件，可以直接用于`gmx_FEL`模块绘制基于dPCA的自由能形貌图。

主成分余弦含量(cosine content)的计算也是对PCA的一种检查。DIP会计算每个PC的余弦含量并输出。当前几个成分的余弦含量的值接近1时，说明该PC可能对应于随机扩散，也即意味着模拟没有收敛，采样较差。关于更多余弦含量的内容，请参考 Berk Hess. Convergence of sampling in protein simulations. Phys. Rev. E 65, 031910 (2002).


## References

如果您使用了DIP的本分析模块，请一定引用GROMACS模拟引擎、DuIvyTools(https://zenodo.org/doi/10.5281/zenodo.6339993)，以及合理引用本文档(https://zenodo.org/doi/10.5281/zenodo.10646113)。

同时请一定引用dPCA的相关文献：
- https://doi.org/10.1002/prot.20310
- https://doi.org/10.1063/1.2746330
