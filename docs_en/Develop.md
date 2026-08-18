# FAQ and Development

## Common Issues

### 1. rdkit Installation Issues

The common method for installing rdkit is through conda. However, we now recommend using pip directly, as pip packages are available for both Windows and Linux, which is faster and less prone to compilation issues compared to conda installation.

Install using pip with the Tsinghua mirror for faster download:

```bash
pip install rdkit -i https://pypi.tuna.tsinghua.edu.cn/simple
```

For more information about the rdkit pip package, visit: https://pypi.org/project/rdkit-pypi

After installation, verify by running the following Python code:

```python
from rdkit import Chem
print(Chem.MolToMolBlock(Chem.MolFromSmiles('C1CCC1')))
```

If no errors occur, the installation is successful.


### 2. Encoding Issues on Windows CMD

Linux systems typically use UTF-8 encoding and rarely encounter encoding issues. However, Windows systems in China commonly use two encodings: UTF-8 and GBK. This can cause encoding errors when DIP executes system commands.

For example, you may encounter the following encoding error in CMD:

```bash
UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 11: illegal multibyte sequence
```

To resolve encoding issues, try the following solutions:

First, check the CMD encoding:

```bash
chcp
```

If the output is 65001, CMD is using UTF-8 encoding. Otherwise, change the encoding:

```bash
chcp 65001
```

This command temporarily switches CMD to UTF-8 encoding.

Additionally, set the Python UTF-8 environment variable:

```bash
set PYTHONUTF8=1
```

You can also set this environment variable in Windows system settings with the variable name `PYTHONUTF8` and value `1`.

These two operations should prevent encoding issues when running DIP commands in CMD.


### 3. How to Change Default Figure Styles?

In most cases, DIP uses DIT from the environment for plotting. In some cases, DIP uses its own plotting functions. You can customize figure styles by modifying the matplotlib style files for DIT and DIP.

Style file locations:

DIT default style file:

```bash
conda_install_location/envs/DIP/Lib/site-packages/DuIvyTools/DuIvyTools/data/mplstyle/DIT.mplstyle
```

DIP default style file:

```bash
conda_install_location/envs/DIP/Lib/site-packages/DuIvyProcedures/data/DIP.mplstyle
```

Users can modify these style files to control figure appearance, such as font sizes, color cycles, etc.:

```txt
## Matplotlib style for DuIvyTools
## https://matplotlib.org/stable/tutorials/introductory/customizing.html#the-matplotlibrc-file

axes.labelsize:     16
axes.linewidth:     1
xtick.labelsize:    16
ytick.labelsize:    16
ytick.left:         True
ytick.direction:    in
xtick.bottom:       True
xtick.direction:    in
lines.linewidth:    2
legend.fontsize:    14
legend.loc:         best
legend.fancybox:    False
legend.frameon:     False
font.family:        Arial
font.size:          16
image.cmap:         coolwarm
image.aspect:       auto # for fitting into axes
# figure.figsize:     6, 5
figure.dpi:         100
savefig.dpi:        300
axes.prop_cycle:    cycler('color', ['38A7D0', 'F67088', '66C2A5', 'FC8D62', '8DA0CB', 'E78AC3', 'A6D854', 'FFD92F', 'E5C494', 'B3B3B3', '66C2A5', 'FC8D62'])
```


### 4. How to View System Commands Called by Analysis Modules?

During analysis, DIP calls DIT and system commands to execute analysis and visualization. Sometimes we need to optimize visualization results or adjust parameters. How can we view the commands used by DIP?

Each DIP analysis module outputs a log file after successful execution. This log file records all commands used, including GROMACS commands and DIT commands. For example:

```bash
[Info] 2024-08-17 17:44:25
>>> run gmx_RMSD module in C:\Users\hhhhh\Desktop\DuIvyProcedures\test\DIP_test\MD
[Info] 2024-08-17 17:44:27
Pid 15264 >>> echo Backbone Protein | gmx rms -s ../md.tpr -f ../md.xtc -n ../index.ndx -o rmsd_Protein2Backbone.xvg -m rmsd_matrix_Protein2Backbone.xpm -tu ns  -dt 1 
[Info] 2024-08-17 17:44:28
Pid 16560 >>> dit xvg_compare -f rmsd_Protein2Backbone.xvg -c 1 -l "" -t "" -ns -o RMSD_Protein2Backbone.png
[Info] 2024-08-17 17:44:31
Pid 6580 >>> dit xpm_show -f rmsd_matrix_Protein2Backbone.xpm -cmap coolwarm -o RMSD_matrix_Protein2Backbone.png -ns


>>>>>> run terminal command log <<<<<<
[Info] 2024-08-17 17:44:27
......
```

This is part of the gmx_RMSD module log file. The first section shows DIP calling the `gmx rms` command for RMSD analysis. The following two commands call DIT's `xvg_compare` and `xpm_show` commands for visualization.

The `command log` section shows the command execution output and related information, which can be used to check error messages.

Users can use this information to adjust and optimize visualization results or verify data correctness.



# Development Plan and Changelog

## Development Plan

### Version 1.0

We will continue to optimize and upgrade existing components and add basic analysis modules.

If you have any suggestions or find any issues, please submit feedback through the link in the WeChat group announcement. DuIvy will try to respond and follow up in a timely manner. Due to limited time, development progress will be relatively slow, but bug fixes may be faster.

Please follow group messages and this page's changelog for version updates.


### Version 1.1

Version 1.1 is planned for release in 2025, which will mainly add more non-covalent analysis modules, membrane-related analysis modules, and possibly some material-related analysis modules. The main framework will include improvements to the logging system and parallel computing capabilities for modules.

Development tasks:
- [ ] More interaction analysis modules
- [ ] Membrane-related analysis
- [ ] Module parallel computing
  

## Changelog

2024.02.04 Completed framework and analysis module development, finished documentation

2024.02.26 Completed multiple rounds of testing and optimization, officially released version 1.0

2024.03.24 Added FEL, Hbond, PiCation, Hydrophobic, MSM and other new components; added new features to existing components; fixed known issues; DIP v1.0 basic functionality completed; released v1.0.2
