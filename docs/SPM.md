# SPM

Shortest Path Map (SPM)是一种分析蛋白质等大分子别构作用和残基的远程联系的有力工具。本模块依照Sílvia Osuna文章（http://dx.doi.org/10.1021/acscatal.7b02954）进行部分复现。

**此模块目前还只是个能跑的demo，后续将会有多轮优化和改进**

## Input YAML

```yaml
- SPM:
    DCCM: "" # DCCM.csv
    Distance_matrix: "" #distance_matrix_average.csv
    type_select: C-alpha # center
    distance_cutoff: 0.6 # nm
    sp_weight_cutoff: 0.3
```

`type_select`: 选择用于计算残基间DCCM和距离矩阵的原子组，可以选择`C-alpha`，或者`center`（残基质心）。

此模块自身具备计算残基间DCCM和距离矩阵的功能，但是用户也可以自定义输入DCCM矩阵和距离矩阵。只需要将`DCCM`和`Distance_matrix`参数写入对应的矩阵csv文件即可；请注意两个矩阵的残基顺序要保持一致，且不要保存header和index。

`distance_cutoff`: 距离矩阵的距离阈值，单位为nm。高于阈值的残基对将不会被graph视作通过edge相连的顶点。

`sp_weight_cutoff`: 最短路径权重的阈值，低于阈值的最短路径将被忽略。

## Output

DIP会输出计算得到的DCCM矩阵、距离矩阵，以及可视化的最短路径图，以及用于pymol的SPM的pml脚本。

![SPM](static/SPM_fig_shortest_paths.png)

SPM也会输出最短路径的权重矩阵，数值越大，表明残基对之间对动态信息的传递越强。


## References

如果您使用了DIP的本分析模块，请一定引用Sílvia Osuna文章（http://dx.doi.org/10.1021/acscatal.7b02954）、MDAnalysis、DuIvyTools(https://zenodo.org/doi/10.5281/zenodo.6339993)，以及合理引用本文档(https://zenodo.org/doi/10.5281/zenodo.10646113)。