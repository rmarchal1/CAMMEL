# Description
The CAlculated-Molecular Multipolar ELectrostatics (CAMMEL) software is an open-source graphical post-treatment software, interfaced with Molcas and OpenMolcas. Various features are implementedin this software such as :
- Wave function decomposition
- Representation of the magnetization curve
- Representation of the Ab initio Transition barriers
- Representation of the susceptibility curve
- Computation and representation of the electrostatic potential surrounding lanthanide atoms <br/>
This Software have been developed in the Institut des Sciences Chimiques de Rennes (ISCR UMR CNRS 6226, University of Rennes1) by Rémi Marchal (Computer engineer), Boris Le Guennic (CNRS Research Director), Guglielmo Fernandez-Garcia (PhD) and Vincent Montigaud (PhD).
# Software Requirement
## OS requirement
Linux or MacOS.</br>
CAMMEL4.0 have been tested on MacOS10.12 and later versions and on Debian and Ubuntu Linux distributions
## Python requirement
CAMMEL is a written in Python3 and pyOpenGL and needs the following python3 libraries to be installed:
- numpy
- matpplotlib
- pyOpenGL
- opencv
- glfw
- Pillow </br>
**Detailed installation instructions can be found in the Manual.**
## Environment variables
CAMMEL needs the folowing environment variables:
- $CAMMEL="directory of the CAMMEL installation"
- Appending PYTHONPATH by "directory of the CAMMEL installation"/source </br>
**Detailed instruction for environment variables settings are given in the Manual.**
## Molcas and OpenMolcas version
CAMMEL have been tested and is compatible with the following versions:
- Molcas80
- Molcas82
- Molcas84
- OpenMolcas18
- OpenMolcas19
# How to run CAMMEL
If the installation process ended properly, you just have to execute the CAMMEL.py with your Python3 interpreter.
# Examples
Examples are provided in the examples directory
# Citations
If you are using CAMMEL, please cite the following papers:
- *Magnetic Slow Relaxation in a Metal–Organic Framework Made of Chains of Ferromagnetically Coupled Single-Molecule Magnets*, G. Huang,G. Fernandez-Garcia,I. Badiane, M. Camarra, S. Freslon, O. Guillou, C. Daiguebonne, F. Totti, O. Cador, T. Guizouarn, B. Le Guennic, K. Bernot, **Chem. Eur. J.**, 2018, 24, 6983
