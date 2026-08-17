# gmx_Cluster

The gmx_Cluster module depends on the `gmx cluster` command to perform cluster analysis on trajectories, and parses the output results of the `gmx cluster` command to generate visualization results, including visualizing the RMSD matrix, cluster size, cluster distribution, etc.

Before using this module, please ensure that the [preprocessing](https://duivyprocedures-docs.readthedocs.io/en/latest/Framework.html#id7) has been completed!

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

`fit_group`: Cluster analysis first requires trajectory alignment. This option is the alignment group, default is `Backbone`.

`calc_group`: The calculation group for cluster analysis, default is `Protein`.

`gmx_parm`: Parameter settings for the `gmx cluster` command, including `method`, `cutoff`, `tu`, `dt`, etc. All available parameters for the `gmx cluster` command can be set here. Some parameters are added by DIP by default, so they do not need to be declared in the yaml file: `-o`, `-g`, `-sz`, `-cl`, and `-clndx`. Trajectory files, tpr files, and ndx files are all input through the yaml Conf section, so they do not need to be input here either.

Please note that if the time step of `gmx cluster`, i.e., `dt`, is set to a short value, there will be more frames to analyze, resulting in larger computation and longer time. At the same time, the output pdb file will also be very large. Please set the corresponding parameters according to your needs.

## Output

After executing this module, DIP will automatically call the `gmx cluster` command and perform clustering. Then DIP will plot rmsd-clust.xpm, clust-size.xvg, and rmsd-dist.xvg.
All result files, visualization images, proportion data and line plots for each cluster, and DIP's log files can be found in the relevant folder under the analysis path.

## References

If you use this analysis module from DIP, please cite GROMACS, DuIvyTools (https://zenodo.org/doi/10.5281/zenodo.6339993), and properly cite this documentation (https://zenodo.org/doi/10.5281/zenodo.10646113).
