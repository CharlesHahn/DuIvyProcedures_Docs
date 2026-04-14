# UMAP

UMAP is a dimensionality reduction method. This module implements UMAP dimensionality reduction based on coordinates and dihedral angles.

Before using this module, please ensure that the [preprocessing](https://duivyprocedures-docs.readthedocs.io/en/latest/Framework.html#id7) has been completed!

## Input YAML

```yaml
- UMAP:
    atom_selection: protein and name CA  # protein for dihedrals 
    byType: atom # res_com, res_cog, res_coc
    n_neighbors: [50, 100, 200, 1000]
    min_dist: [1]
    target: coordinates  # dihedrals
- UMAP:
    mkdir: UMAP2
    atom_selection: protein # protein for dihedrals 
    byType: atom # res_com, res_cog, res_coc
    n_neighbors: [50]
    min_dist: [1, 2, 5, 10]
    target: dihedrals
```

Here we list the parameters for both coordinate-based and dihedral-based UMAP analysis.

`atom_selection`: Atom selection for specifying the atom group for UMAP. If performing dihedral analysis, the selected atom group must contain atoms that form backbone dihedral angles. The atom selection syntax here follows MDAnalysis atom selection syntax. Please refer to: https://userguide.mdanalysis.org/2.7.0/selections.html

`byType`: Specifies the method for coordinate-based dimensionality reduction, only effective when `target` is `coordinates`. There are four options: `atom`, `res_com`, `res_cog`, `res_coc`. `atom` calculates dimensionality reduction of all selected atom coordinates; commonly, you can select CA atoms in `atom_selection` with `protein and name CA` to calculate protein dimensionality reduction; `res_com` calculates dimensionality reduction of each residue's center of mass; `res_cog` calculates dimensionality reduction of each residue's geometric center; `res_coc` calculates dimensionality reduction of each residue's charge center. When using `res_com`, `res_cog` or `res_coc`, the atom selector should contain all atoms of the selected residues, otherwise only the center of mass, geometric center, or charge center of selected atoms within a residue will be calculated.

`target`: The target for UMAP, can be `coordinates` or `dihedrals`. If `coordinates` is selected, UMAP will be based on atom coordinates; if `dihedrals` is selected, UMAP will be based on dihedral angles.

**Note**: The dPCA literature discusses that dihedral angles differ from coordinates - dihedral angles are periodic. Therefore, dPCA articles apply trigonometric transformation to angles before PCA analysis. This module also converts dihedral angles to sin and cos values before dimensionality reduction analysis. **Users performing dihedral angle dimensionality reduction analysis with this module should carefully compare with the literature to verify if the calculation process is appropriate! If uncertain, please do not use this module's dihedral angle dimensionality reduction analysis** For any questions or improvement suggestions, please contact Du Ruo. Du Ruo and Du Ivy welcome any suggestions and arguments. Thank you very much!

`n_neighbors`: Number of neighbors, used to specify the number of neighbors for each point in the UMAP algorithm. Since it's usually not possible to know a priori what parameter setting is appropriate, you can write multiple possible parameters in a list here, and DIP will iterate through each parameter to generate results for selection.

`min_dist`: Controls how tightly points are clustered.

For specific parameter settings, please refer to the UMAP official documentation and https://doi.org/10.1063/5.0099094

This module also has three hidden parameters for frame selection:

```yaml
      frame_start:  # start frame index
      frame_end:   # end frame index, None for all frames
      frame_step:  # frame index step, default=1
```

These parameters can specify the start frame, end frame (exclusive), and frame step for trajectory calculation. By default, users do not need to set these parameters, and the module will automatically analyze the entire trajectory.

For example, to calculate DCCM from frame 1000 to frame 5000, every 10 frames:

```yaml
      frame_start: 1000 # start frame index
      frame_end:  5001 # end frame index, None for all frames
      frame_step: 10 # frame index step, default=1
```

If only one or two of the three parameters need to be set, the others can be omitted.


## Output

This module plots the 2D data from dimensionality reduction as scatter plots. Here are examples of coordinate-based and dihedral-based UMAP results, with parameters `n_neighbors=50, min_dist=1`:

![UMAP_coordinates](static/umap12_coordinates_n_neighbors_50_min_dist_1.png)

![UMAP_dihedrals](static/umap12_dihedrals_n_neighbors_50_min_dist_1.png)


## References

If you use this analysis module from DIP, please cite MDAnalysis, UMAP (https://doi.org/10.1162/neco_a_01434), DuIvyTools (https://zenodo.org/doi/10.5281/zenodo.6339993), and properly cite this documentation (https://zenodo.org/doi/10.5281/zenodo.10646113).
