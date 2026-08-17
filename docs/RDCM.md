# RDCM

This module is mainly used for residue distance contact matrix analysis. Based on residue distances, many interesting analyses can be extended, including observing protein structural changes, calculating RMSD, RMSF, DCCM, PCA, clustering based on residue distance contact matrices, and calculating correlations between residue distances and other variables. This module also supports defining contacts and calculating contact formation time occupancy and other data, as well as custom encounters and calculating time occupancy and cross-correlation information based on encounters.

Reference: https://zhuanlan.zhihu.com/p/578885815

Before using this module, please ensure that the [preprocessing](https://duivyprocedures-docs.readthedocs.io/en/latest/Framework.html#id7) has been completed!

## Input YAML

```yaml
- RDCM:
    type_select: center # atom # min
    atom_selection: protein
    frames_output_step: -1 # -1 for no output
    calc_RMSD: no
    RMSD_Matrix_step: -1 # -1 for no output
    calc_RMSF: no
    calc_DCCM: no
    Pearson_Observe: "" # ../RMSD.xvg
    calc_PCA: no
    clustering_step: -1 # -1 for no clustering
    calc_contact: yes
    contact_cutoff: 1.5
    calc_encounter: yes
    encounter_low_cutoff: 0.8
    encounter_high_cutoff: 1.0
    calc_encounter_DCCM: no
```

The above is the input YAML file for the RDCM module. Below is a detailed explanation of each parameter:

`type_select`: Select the type for calculating residue contact distance matrix. `center` means using residue centroid, `atom` means using atom coordinates, `min` means using minimum distance between residues. When using `center` or `min`, please include all atoms of residues in atom selection, otherwise only centroid distance or minimum distance of selected atoms within residues will be calculated.

**Note: If `min` type is selected, the calculation will be very slow!** You can combine with the frame selection parameters below to reduce the number of frames to calculate.

Starting from v1.0.3, `type_select` supports `res_com`, `res_cog`, `res_coc`, `res_min`, and `atom` parameters. The previous `center`, `atom`, `min` parameters are also still supported, where `center` is equivalent to `res_com`, `min` is equivalent to `res_min`. `res_com`, `res_cog`, `res_coc`, and `res_min` represent using residue center of mass, geometric center, charge center, and minimum distance between residue atom pairs to calculate distance matrix respectively.

If the protein is large and has many frames, it is recommended to combine with frame selection parameters below to reduce computation, otherwise there may be insufficient memory.

`atom_selection`: Select the atom group for calculating residue contact distance matrix. If `type_select` is `center`, residue centroid will be calculated directly; if `type_select` is `atom`, residue distance will be calculated based on this atom's coordinates, so selecting multiple atoms of one residue is not recommended; if `type_select` is `min`, calculation will be by residue.

`frames_output_step`: Step for outputting contact matrices, i.e., output contact matrix every how many frames. `-1` means not outputting contact matrices. If the trajectory has n frames, RDCM also has n frames. Outputting all will be time-consuming, so it is recommended to set a larger output step to save time. In output frames, DIP will also calculate the difference between two frames of matrices, representing the change of RDCM matrix between two frames.

`calc_RMSD`: Whether to calculate RMSD based on RDCM.

`RMSD_Matrix_step`: `-1` means not calculating RMSD matrix based on RDCM; when the value is positive, DIP will calculate RMSD matrix and output according to the set frame step. When the step is too small, the time for calculating RMSD matrix will increase significantly!

`calc_RMSF`: Whether to calculate RMSF based on RDCM.

`calc_DCCM`: Whether to calculate DCCM based on RDCM.

`Pearson_Observe`: This module by default calculates Pearson correlation coefficients between pairwise residue distances and time to characterize the co-variation trend of residue distances and time. Similarly, users can customize variables for calculating Pearson correlation coefficients, such as setting a key distance or RMSD value. Custom variable input needs to be in xvg file format, with the first column being time and the second column being the variable value over time. Please note that the dimension of this variable (number of data points over time) needs to be consistent with the number of trajectory frames!

`calc_PCA`: Whether to calculate PCA based on RDCM.

`clustering_step`: `-1` means not performing residue and frame clustering based on RDCM; when the value is positive, this module will perform frame clustering and output according to the set step, and will also cluster residues. When the step is too small, there may be many frames to cluster, which will increase time consumption and the final visualization effect may not be good.

`calc_contact`: Whether to calculate contact based on RDCM.

`contact_cutoff`: Defines the distance threshold for contact, i.e., two residues with distance less than this threshold are considered as contact.

`calc_encounter`: Whether to calculate encounter based on RDCM.

`encounter_low_cutoff` and `encounter_high_cutoff`: Encounter can be considered as a stricter contact; when residue distance is less than `encounter_low_cutoff`, it is considered as forming an encounter; when distance is greater than `encounter_high_cutoff`, it is considered as encounter breaking. These two thresholds can be set according to the literature!

`calc_encounter_DCCM`: Whether to calculate DCCM based on encounter matrix.

This module also has three hidden parameters for frame selection:

```yaml
      frame_start:  # start frame index
      frame_end:   # end frame index, None for all frames
      frame_step:  # frame index step, default=1
```

These parameters can specify the start frame, end frame (exclusive), and frame step for trajectory calculation. By default, users do not need to set these parameters, and the module will automatically analyze the entire trajectory.

For example, to calculate from frame 1000 to frame 5000, every 10 frames:

```yaml
      frame_start: 1000 # start frame index
      frame_end:  5001 # end frame index, None for all frames
      frame_step: 10 # frame index step, default=1
```

If only one or two of the three parameters need to be set, the others can be omitted.

## Output

Below is an explanation of results with a specific input. Here we calculated the distance matrix of all residue centroids for a protein, with 10001 frames and 130 residues:

```yaml
- RDCM:
    type_select: center
    atom_selection: protein
    type_min_spend: time # memory
    type_min_step: 1 # for step to calc min dist
    frames_output_step: 1000 # -1 for no output
    calc_RMSD: yes
    RMSD_Matrix_step: 100 # -1 for no output
    calc_RMSF: yes
    calc_DCCM: yes
    Pearson_Observe: "RDCM_RMSD.xvg" # ../RMSD.csv
    calc_PCA: yes
    clustering_step: 1000 # -1 for no clustering
    contact_cutoff: 1.5
    encounter_low_cutoff: 0.8
    encounter_high_cutoff: 1.0
    calc_encounter_DCCM: yes
```

First, DIP will output the initial and final frames of RDCM. Intermediate frames output every 1000 frames will be saved to the RDCM_frames folder. **Matrices will be output to both csv files and xpm files, and visualized.**

Initial frame:
![RDCM_initial_frame](static/RDCM_Distance_First.png)


Final frame:
![RDCM_final_frame](static/RDCM_Distance_Last.png)

A certain intermediate output frame:
![RDCM_middle_frame](static/RDCM_Distance_Time_60000.0.png)

Difference between intermediate frame and its previous frame:
![RDCM_diff](static/RDCM_Distance_Time_60000.0-50000.0.png)

DIP will also calculate the average and standard deviation of all RDCM frames and output:

Average:
![RDCM_ave](static/RDCM_Distance_Average.png)

Standard deviation:
![RDCM_std](static/RDCM_Distance_Deviation.png)

If `calc_RMSD` is set to `yes`, the RMSD curve based on RDCM will be calculated:
![RDCM_RMSD](static/RDCM_RMSD.png)

If RMSD matrix output is set, the RMSD matrix will be output:
![RDCM_RMSD_Matrix](static/RDCM_RMSD_Matrix.png)

If `calc_RMSF` is set to `yes`, the RMSF curve based on RDCM will be calculated:
![RDCM_RMSF](static/RDCM_RMSF.png)

If `calc_DCCM` is set to `yes`, the DCCM matrix based on RDCM will be calculated:
![RDCM_DCCM](static/RDCM_DCCM.png)

DIP by default calculates Pearson correlation coefficients between residue distances and time and outputs the correlation matrix:
![RDCM_Pearson_Time](static/RDCM_Pearson_Time.png)

Since p_values can be obtained from Pearson correlation coefficient calculation, there is also a corresponding p_value matrix:
![RDCM_Pearson_Time_pvalue](static/RDCM_Pearson_Time_p_Value.png)

If `Perason_Observe` is set, Pearson correlation coefficients between residue distances and custom variables will also be calculated. Here in the example, we used RMSD data based on RDCM, yielding the following output:
![RDCM_Pearson_RMSD](static/RDCM_Pearson_Observe.png)

P-value matrix for Pearson correlation with RMSD:
![RDCM_Pearson_RMSD_pvalue](static/RDCM_Pearson_Observe_p_Value.png)

If `calc_PCA` is set to `yes`, PCA based on RDCM will be calculated, yielding scatter plots of three principal components:
![RDCM_PCA12](static/RDCM_PCA12.png)
![RDCM_PCA13](static/RDCM_PCA13.png)
![RDCM_PCA23](static/RDCM_PCA23.png)

Here we also set the clustering step, so there will be residue clustering and frame clustering plots:
![RDCM_Clustering_Frame](static/RDCM_Time_dendrogram.png)
![RDCM_Clustering_Residue](static/RDCM_Residues_dendrogram.png)

Below is the contact section, including contact occupancy matrix:
![RDCM_Contact_Occupancy](static/RDCM_Contact_Time_Occupancy.png)

And converting contact matrix occupancy to one dimension to obtain the so-called local contact time curve, which can reflect local contact stability:
![RDCM_Contact_Time](static/RDCM_contact_occupancy_curve.png)

The contact section will also calculate several dimensionless numbers, such as C50: the proportion of residue pairs with contact time occupancy exceeding 50% to total residue pairs. Results can be seen in screen output or log:
```txt
>>> C50 of contact matrix: 0.6702317290552585
>>> C70 of contact matrix: 0.6292335115864528
>>> C90 of contact matrix: 0.5583778966131907
```

Finally is the Encounter section.

First, the first formation time matrix of Encounter:
![RDCM_Encounter_Time_First](static/RDCM_Encounter_FirstTime.png)

Last formation time matrix:
![RDCM_Encounter_Time_Last](static/RDCM_Encounter_LastTime.png)

Average formation time matrix:
![RDCM_Encounter_Time_Average](static/RDCM_Encounter_AvesTime.png)

Average time length matrix of Encounter:
![RDCM_Encounter_Time_Length](static/RDCM_Encounter_TimeLens.png)

Encounter time occupancy matrix:
![RDCM_Encounter_Occupancy](static/RDCM_Encounter_Time_Occupancy.png)

Similar local Encounter curve:
![RDCM_Encounter_Occupancy_Curve](static/RDCM_encounter_occupancy_curve.png)

Matrix of number of Encounter formations:
![RDCM_Encounter_Count](static/RDCM_Encounter_Count.png)

There are also several dimensionless numbers with slightly different meanings, for example C50: the total time of encounters with time occupancy exceeding 50% as a proportion of total time of all encounters. Results can be seen in screen output or log:
```txt
>>> C50 of encounter matrix: 0.8080651265333009
>>> C70 of encounter matrix: 0.7812075139181635
>>> C90 of encounter matrix: 0.7155487165048366
```

Finally, the DCCM matrix based on Encounter:
![RDCM_Encounter_DCCM](static/RDCM_Encounter_DCCM.png)


## References

If you use this analysis module from DIP, please cite MDAnalysis, CONAN (https://doi.org/10.1016/j.bpj.2018.01.033), DuIvyTools (https://zenodo.org/doi/10.5281/zenodo.6339993), and properly cite this documentation (https://zenodo.org/doi/10.5281/zenodo.10646113).