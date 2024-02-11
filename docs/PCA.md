# PCA

此模块可以用于计算所选原子组的主成分分析（PCA）。可以对坐标进行主成分分析，也可以对蛋白质骨架二面角做PCA。


## Input YAML

```yaml
- PCA:
    atom_selection: protein and name CA
    target: coordinates # dihedrals
- PCA:
    mkdir: PCA_d
    atom_selection: protein
    target: dihedrals
```

这里同时列举了基于坐标和基于二面角的PCA分析所需要的参数。

`atom_selection`：原子选择，用于指定需要进行PCA的原子组。如果进行二面角分析的话，则所选的原子组必须包含形成骨架二面角的原子。这里的原子选择的语法完全遵从MDAnalysis的原子选择语法。请参考：https://userguide.mdanalysis.org/1.1.1/selections.html

`target`：PCA的目标，可以是`coordinates`或`dihedrals`。如果选择`coordinates`，则PCA将基于原子的坐标进行分析；如果选择`dihedrals`，则PCA将基于二面角进行分析。

**需要注意的是**：dPCA的文献中讨论到二面角与坐标不同，二面角具有周期性；因而dPCA的文章中是对角度进行了三角变换再将之应用于PCA分析，而此模块并不包含二面角的三角变换过程，而是直接对角度值继续了PCA的计算。**用户在进行dPCA分析的时候，需要妥善对照文献分析计算过程是否合适！** 有任何问题或者改进的建议，请联系杜若，杜若和杜艾维非常欢迎任何的建议和argue，非常感谢！。

## Output

DIP在对体系进行PCA分析之后，会将前三个主成分的数值保存到xvg文件中，并对主成分进行两两的散点图可视化。

基于坐标的PCA的前两个主成分：

![PCA_coordinates](static/PCA_pca12.png)

基于Dihedral的PCA的前两个主成分：

![PCA_dihedrals](static/PCA_d_pca12.png)


需要注意的是，**前三个主成分的占比输出在屏显或者log中**：

```txt
The ratio of engenvalues -> [0.35126355 0.25190672 0.049121  ]
```


## References

如果您使用了DIP的本分析模块，请一定引用MDAnalysis、scikit-learn(https://scikit-learn.org/stable/about.html#citing-scikit-learn)、DuIvyTools(https://zenodo.org/doi/10.5281/zenodo.6339993)，以及合理引用本文档(https://zenodo.org/doi/10.5281/zenodo.10646113)。
