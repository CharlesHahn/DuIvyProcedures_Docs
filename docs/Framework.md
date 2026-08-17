# FrameWork 

DIP consists of several parts: analysis modules, control modules, and input control modules.

## Analysis Modules

Analysis modules are mainly modules that execute analyses, containing code for performing various analyses and generating analysis results.


## Control Modules

Control modules contain functions for serial execution of various analyses, path control, parameter control, log recording, etc.

## Input Control Modules

DIP uses YAML format files to store parameter information for user-input analysis modules. This file contains GROMACS paths, trajectory files, topology files, paths where analyses need to be executed, and the names and related parameters of analysis tasks to be executed.

**Please note! DIP will not perform periodic correction on user trajectories. Please correct trajectories yourself first to ensure molecular integrity and reasonable relative positions!**

### Generating Parameter Files

Users can generate a parameter file containing all analysis modules with the following command:

```bash
dip conf -o dip.yaml
```

Or you can specify the analysis methods to perform or the paths to analyze through `-t` or `-d` commands:

```bash
dip conf -o dip.yaml -t gmx_RMSD DCCM -d MD0
```

### Modifying Parameter Files

Generally, the default generated parameter file **is not ready to use out of the box**. Users need to modify it according to actual situations.

Common places that need modification include: the path to the gmx executable, names of trajectory files and topology files, paths for executing analyses (these paths must contain the set trajectory files and topology files), and input parameters for various analysis modules.

Please refer to the input parameter yaml file parsing below and the input parameters section for corresponding analysis modules.


### Using Parameter Files

To execute analyses, please run:

```bash
dip run -f dip.yaml
```

DIP will execute analysis tasks in order of analysis paths and analysis modules, and save results in corresponding analysis directories.

### User Input YAML File Content Parsing


The YAML file for user input needs to contain at least the following three parts:

```yaml
Path:
 - MD0
 - MD1
 - MD2

Conf:
  gmx: gmx
  xtc: md.xtc
  tpr: md.tpr
  ndx: index.ndx

Tasks:
  - gmx_RMSD:
      fit_group: Backbone
      calc_group: Protein
      rmsd_matrix: no
      gmx_parm:
        tu: ns
```

The Path section is used to specify analysis paths; multiple paths can be specified; DIP will analyze trajectories under each path in sequence;

The Conf section is used to configure GROMACS path, input file names, index file names, etc.; these files under different analysis paths need to have consistent names. For example, for two different simulation systems, MD0 and MD1, the trajectory files in their directories both need to be named md.xtc to be read and analyzed by DIP.

For analysis tasks that do not depend on GROMACS (analysis modules not starting with `gmx_`), trajectory files and topology files can be in other formats, such as Amber format trajectory and topology files, which DIP can also recognize.

Starting from v1.0.3, the Conf section can also add a parameter `fig` to control output image format. By default, output images are in PNG format. You can set the `fig` parameter to `pdf`, `svg`, etc. to output images in multiple formats. For example:

```yaml
Conf:
  gmx: gmx
  xtc: md.xtc
  tpr: md.tpr
  ndx: index.ndx
  fig: pdf
```

The Tasks section is used to specify specific analysis tasks. Each task has its own parameters, and specific analysis tasks are determined by the specific implementation of analysis modules.

The first line of the Tasks section is the name of the analysis module, and below are parameters belonging to that analysis module. For example, the gmx_RMSD module here needs parameters like fit_group to be set.

The gmx_parm parameter here can contain relevant parameters for the gmx command that this analysis module depends on. For example, the gmx rmsd command can have parameters like `-b -e -tu`, which can be set here as:

```yaml
gmx_parm:
  b: 0
  e: 10000
  tu: ns
```

DIP will directly append the parameters set under gmx_parm to the gmx command for execution. Of course, the `gmx_parm` parameter is not mandatory if you don't need to add extra parameters.

Each analysis module has a hidden parameter: `mkdir`. If we execute the same analysis with two different parameters simultaneously, the analysis results need to be placed in different folders. Therefore, the `mkdir` parameter can specify a folder name to place the analysis results in that folder. By default, the `mkdir` parameter is the name of the analysis module.

```yaml
Tasks:
  - gmx_RMSD:
      fit_group: Backbone
      calc_group: Protein
      rmsd_matrix: no
      gmx_parm:
        tu: ns
  - gmx_RMSD:
      mkdir: gmx_RMSD2
      fit_group: Protein
      calc_group: Protein
      rmsd_matrix: yes
```

For all analysis modules that depend on GROMACS, the values of group selection parameters must be groups that naturally exist in the simulation system, such as `System`, `Protein`, `Backbone`, etc., or groups defined by users through GROMACS index files.

**Please note that all group names must start with English letters, have no spaces, and cannot start with numbers!** Groups starting with numbers, such as `6Lig`, will be recognized by GROMACS as the 6th group instead of the 6Lig group.

All analysis modules that do not depend on GROMACS (not starting with `gmx_`) also have three hidden parameters for frame selection:

```yaml
      frame_start:  # start frame index
      frame_end:   # end frame index, leave blank for all frames
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

Parameters for other analysis modules are similar. Please refer to the documentation for specific analysis modules.


## Preprocessing

Some processing needs to be done by users themselves before running analysis with DIP.

1. If users use gmx-based modules, they need to prepare topology files and trajectory files, as well as index files themselves. Please note that trajectory files need **periodic correction by users themselves** to ensure molecular integrity and reasonable relative positions. Also, groups and names in index files need to be generated by users themselves.

2. If users use MDAnalysis-based modules, they need to prepare topology files and trajectory files themselves. Please note that trajectory files need **periodic correction by users themselves** to ensure molecular integrity and reasonable relative positions. **The number of atoms in topology files and trajectory files must correspond one-to-one**, otherwise MDAnalysis cannot read them.

3. Since GROMACS 2024 has many changes in analysis commands, analysis modules in DIP that depend on GROMACS may not be suitable for GROMACS 2024. GROMACS 2019 to 2023 versions are recommended. Additionally, for GROMACS 2022 and earlier versions, running DIP's `gmx_DSSP` module depends on the `gmx do_dssp` command, so users need to ensure that DSSP is properly installed and the `gmx do_dssp` command is available. When running the `PiStacking` module, if DIP needs to automatically find possible aromatic rings, please ensure that rdkit is properly installed and callable.