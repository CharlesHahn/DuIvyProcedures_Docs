# Density

此模块计算所选原子的质量和电荷密度沿X、Y、Z方向的分布。

## Input YAML

```yaml
- Density:
    calc_group: protein  # resname *ZIN
```

`calc_group`：选择计算的原子组，语法完全遵从MDAnalysis的语法。


## Output

DIP会输出质量密度和电荷密度在X、Y、Z方向的分布图以及相应的数据文件（xvg格式）。

![Mass density](static/Density_Mass_density_XYZ.png)

![charge density](static/Density_Charge_density_XYZ.png)


## References

如果您使用了DIP的本分析模块，请一定引用MDAnalysis、DuIvyTools(https://zenodo.org/doi/10.5281/zenodo.6339993)，以及合理引用本文档。
