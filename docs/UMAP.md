# UMAP

UMAP是一种降维方法，此模块实现了基于坐标的和基于二面角的UMAP降维。

## Input YAML

```yaml
- UMAP:
    atom_selection: protein and name CA  # protein for dihedrals 
    n_neighbors: [50, 100, 200, 1000]
    min_dist: [1]
    target: coordinates  # dihedrals
- UMAP:
    mkdir: UMAP2
    atom_selection: protein # protein for dihedrals 
    n_neighbors: [50]
    min_dist: [1, 2, 5, 10]
    target: dihedrals
```

这里同时列举了基于坐标和基于二面角的UMAP分析所需要的参数。

`atom_selection`：原子选择，用于指定需要进行UMAP的原子组。如果进行二面角分析的话，则所选的原子组必须包含形成骨架二面角的原子。这里的原子选择的语法完全遵从MDAnalysis的原子选择语法。请参考：https://userguide.mdanalysis.org/1.1.1/selections.html

`target`：UMAP的目标，可以是`coordinates`或`dihedrals`。如果选择`coordinates`，则UMAP将基于原子的坐标进行分析；如果选择`dihedrals`，则UMAP将基于二面角进行分析。

`n_neighbors`：近邻数量，用于指定UMAP算法中每个点的近邻数量, 通常可能无法先验的知道参数设置成多少比较合适，因而这里可以在一个列表中写入多个可能的参数，DIP会遍历每种参数生成结果供选择。

`min_dist`: 控制点堆积的紧密程度。

关于具体的参数的设置，可以参考UMAP的官方文档，以及 https://doi.org/10.1063/5.0099094

## Output

此模块会将降维得到的2维数据绘制成散点图，这里列举了基于坐标和基于二面角的UMAP的结果，其中参数为`n_neighbors=50, min_dist=1`：

![UMAP_coordinates](static/umap12_coordinates_n_neighbors_50_min_dist_1.png)

![UMAP_dihedrals](static/umap12_dihedrals_n_neighbors_50_min_dist_1.png)


## References

如果您使用了DIP的本分析模块，请一定引用MDAnalysis、UMAP(https://doi.org/10.1162/neco_a_01434)、DuIvyTools(https://zenodo.org/doi/10.5281/zenodo.6339993)，以及合理引用本文档(https://zenodo.org/doi/10.5281/zenodo.10646113)。