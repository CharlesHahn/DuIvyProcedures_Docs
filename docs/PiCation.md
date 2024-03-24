# PiCation

此模块用于分析Pi-阳离子相互作用。

使用本模块前请注意[前置处理](https://duivyprocedures-docs.readthedocs.io/en/latest/Framework.html#id7)已经完成！

## Input YAML

```yaml
- PiCation:
    distance_max_cutoff: 0.60
    distance_min_cutoff: 0.05
    ring_center_offset: 0.20
    byIndex: no 
    group4PiRing: protein
    group4Cation: protein
    only_aromatic_rings: no
    other_ring_max_atom_num: 7
    planarity_cutoff: 5  ## degree, 5 deg for planar
    NH3_atomnames: ["N", "H1", "H2", "H3"]
    COO_atomnames: ["C", "O1", "O2"]
    Backbone_atomnames: ["H", "N", "CA", "C", "O"]
    ignore_chain_end: no
    Pi_rings_Index: [[ 24,  25,  27,  29,  31,  33], 
      [249, 250, 252, 254, 256, 258],
      [474, 475, 477, 479, 481, 483], 
      [699, 700, 702, 704, 706, 708],
      [924, 925, 927, 929, 931, 933],
      [ 41,  42,  44,  46,  48,  50],
      [266, 267, 269, 271, 273, 275],
      [491, 492, 494, 496, 498, 500], 
      [716, 717, 719, 721, 723, 725],
      [941, 942, 944, 946, 948, 950]]
    cation_Index: [[118,119,120,121], [343,344,345,346], 
      [568,569,570,571], [793,794,795,796], [1018,1019,1020,1021]]
    calc_lifetime: no
    tau_max: 50  # frame
    window_step: 1 # frame
    intermittency: 0  # allow 0 frame intermittency
```

同前面的盐桥分析模块一样，这里也提供了两种方式去定义可形成PiStacking的环。第一种是通过索引，第二种是DIP通过rdkit去判别。

`distance_max_cutoff`：定义PiCation相互作用距离的最大值，单位为纳米。

`distance_min_cutoff`：定义PiCation相互作用距离的最小值，单位为纳米。

`ring_center_offset`：定义环中心偏移量，单位为纳米。offset定义为Cation的电荷中心在环的平面上的投影，与环的质心的距离。

`byIndex`：是否通过索引定义可形成PiCation的环和Cation基团。如果`yes`，则`Pi_rings_Index`和`cation_Index`必须提供对应的原子索引。如果`no`, 则DIP自行寻找。

`group4PiRing`和`group4Cation`：定义两个原子组，用于从中寻找芳香环和Cation结构。这两个参数只有当`byIndex`为`no`时才有效。DIP会自动从第一个组中探测芳香环结构，从第二个组中探测Cation结构；并计算两者之间的PiCation；如果需要计算组内的PiCation，可以两个组写成同样的原子组。这里的原子选择的语法完全遵从MDAnalysis的原子选择语法。请参考：https://userguide.mdanalysis.org/1.1.1/selections.html

`only_aromatic_rings`：当DIP自动寻找可形成PiStacking的环时，是否只考虑芳香环（环上每一根键都是芳香键），还是考虑所有环。**非芳香环极有可能存在误判，因而需要用户对结果进行检查！**

`other_ring_max_atom_num`：当DIP自动寻找可形成PiStacking的环时，对于没有被判别为芳香环的环，其最大允许的原子数量。其最小允许的原子数量为5。

`planarity_cutoff`：当DIP自动寻找可形成PiStacking的环时，对于没有被判别为芳香环的环，其允许的平面度；DIP会计算环上所有原子与其邻居原子的法向，任意两个法向之间的夹角需要小于这里设定的值才会被判别为平面环，并被DIP当作可形成PiStacking的环加以计算。**请注意，平面环并不等于芳香环，还请自行根据输出的环的pdb文件加以检查！**

如果`byIndex`为`no`的话，则DIP会根据体系的电荷去寻找可能形成盐桥的原子组。但是考虑到不同的力场条件下原子的名称可能不同，并且未形成肽键的C或者N端也有可能形成盐桥。因而这里可能需要用户根据使用的力场去填写一下COO-和NH3+的原子名称，以帮助程序正确判断所有带电基团。

`ignore_chain_end`：是否忽略链端残基，设置为`yes`则程序会忽略链端残基，只计算链中段的带电基团。

`calc_lifetime`：是否计算PiCation的生命周期。

`tau_max`：生命周期的最大时间，单位为帧。计算生命周期的过程中会计算从t0时刻开始，`tau_max`帧内，PiCation继续存在的概率。此值设置越大，则计算的窗口越大。

`window_step`：生命周期的窗口平移步长，单位为帧。

`intermittency`：允许的帧间隔，即允许多少帧没有发生PiCation仍旧视为PiCation；默认为0，即必须连续发生才被视为PiCation。

本模块还有三个隐藏参数可以对轨迹做帧的选择：

```yaml
      frame_start:  # start frame index
      frame_end:   # end frame index, None for all frames
      frame_step:  # frame index step, default=1
```

这些参数可以指定计算轨迹的起始帧、终止帧（不包含）以及帧的步长。默认情况下，用户不需要设置这些参数，模块会自动分析整个轨迹。

例如我们计算从1000帧开始，到5000帧结束，每隔10帧的DCCM：

```yaml
      frame_start: 1000 # start frame index
      frame_end:  5001 # end frame index, None for all frames
      frame_step: 10 # frame index step, default=1
```

如果三个参数中只需要设置一个或两个，其余的参数都可以省略。

## Output

首先是输出DIP判定的可形成PiCation的环和Cation基团，以供用户判断正确性。DIP会将之输出成pdb文件，用户可以自行检查。同时DIP还会输出各个环和Cation基团及其对应的原子索引到txt文件，供用户进一步确认和重复利用：

```txt
PiStacking_Names, Indexs
PHE3, [24, 25, 27, 29, 31, 33]
PHE4, [41, 42, 44, 46, 48, 50]
PHE29, [249, 250, 252, 254, 256, 258]
PHE30, [266, 267, 269, 271, 273, 275]
PHE55, [474, 475, 477, 479, 481, 483]
Cations_Names, Indexs
LYS12, [118, 119, 120, 121]
LYS38, [343, 344, 345, 346]
LYS64, [568, 569, 570, 571]
LYS90, [793, 794, 795, 796]
LYS116, [1018, 1019, 1020, 1021]
```


之后会输出所有PiCation的Pi质心到Cation电荷中心的距离、偏移量等数据到xvg文件，并可视化：

![Pistacking_Distance](static/PiCation_Distances.png)

![PiCation_Offset](static/PiCation_Offsets.png)

之后会输出所有PiCation的占有率图：

![PiCation_Occupancy](static/PiCation_Existence_Map.png)


所有PiCation的汇总信息可以在输出的csv文件中找到：

```csv
id,Name,Occupancy,Frames/Total,Distance(nm),Offset(nm)
0,PHE3-LEU1_NH3,1.11%,111/10001,0.556403,0.145827
1,PHE29-LEU27_NH3,0.01%,1/10001,0.581956,0.158579
2,PHE55-LEU53_NH3,0.01%,1/10001,0.599074,0.190308
3,PHE81-LEU79_NH3,0.11%,11/10001,0.535019,0.159096
4,PHE107-LEU105_NH3,0.06%,6/10001,0.564249,0.136644
5,2ZIN132-LYS12,0.24%,24/10001,0.529427,0.146480
6,2ZIN132-LEU1_NH3,3.48%,348/10001,0.564333,0.119180
7,2ZIN132_13-LEU1_NH3,0.24%,24/10001,0.557451,0.147649
8,6ZIN136-LYS116,1.82%,182/10001,0.563790,0.137136
9,6ZIN136_21-LYS116,0.11%,11/10001,0.440715,0.171171

```

如果计算生命周期，则自相关函数会被输出并可视化；同时自相关函数的积分，也即生命周期，也会被输出到csv文件中。请注意，这里的生命周期是直接对自相关函数数据进行simpson积分得到的，准确度一般。

如果观察到在自相关函数的自变量范围内函数值还没有降到0，说明应当适当调大`tau_max`参数以获得更准确的生命周期积分。

## References

如果您使用了DIP的本分析模块，请一定引用MDAnalysis、rdkit，DuIvyTools(https://zenodo.org/doi/10.5281/zenodo.6339993)，以及合理引用本文档(https://zenodo.org/doi/10.5281/zenodo.10646113)。