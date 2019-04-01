<div align="center">
<img src="https://github.com/cemac/cemac_generic/blob/master/Images/cemac.png">
<a href="https://africanswift.org/">
  <img src="https://github.com/cemac/SWIFTDB/blob/master/static/SWIFT-logo.jpg"></a>
  <br>
</div>

 <h1> <center> MARTIN SWIFT GUI </center> </h1>

[![DOI](https://zenodo.org/badge/169722642.svg)](https://zenodo.org/badge/latestdoi/169722642) [![GitHub release](https://img.shields.io/github/release/cemac/MARTIN.svg)](https://github.com/cemac/MARTIN/releases) [![GitHub top language](https://img.shields.io/github/languages/top/cemac/MARTIN.svg)](https://github.com/cemac/MARTIN) [![GitHub issues](https://img.shields.io/github/issues/cemac/MARTIN.svg)](https://github.com/cemac/MARTIN/issues) [![GitHub last commit](https://img.shields.io/github/last-commit/cemac/MARTIN.svg)](https://github.com/cemac/MARTIN/commits/master) [![GitHub All Releases](https://img.shields.io/github/downloads/cemac/MARTIN/total.svg)](https://github.com/cemac/MARTIN/releases)


A python graphical user interface for the viewing of model and satellite imagery. MARTIN allows for annotations to be made and the resultant images/annotations to be saved.

This work forms part of the Global Challenged Research Fund (GCRF) [African SWIFT (Science for Weather Information and Forecasting Techniques) project.](https://africanswift.org/)


:construction: documentation in progress :construction:

# Requirements (USERS)

* Platforms: Windows or Linux OS

# Installation (USERS)

1. Download and extract MARTIN
2. Use the specific folder structure outlined in MARTIN_IMAGE_ANNOTATIONS
3. It is possible to request example image data (Collaborators only)

# Usage (USERS)

**See Full USER Guide in [docs/USER_GUIDE.pdf](docs/USER_GUIDE.pdf)**
* `MARTIN_WINDOWS.exe` (Windows OS)
* `MARTIN_Linux` (linux)
* Execute appropriate file
* Select “Source” (model from which images were generated), “Region” (for testbed 1a
these are EA; East Africa, WA; West Africa and TropA; Tropical Africa), “Init”
(initiation time of simulation), “Var” (variable you want to see image of and “Time”
(the forecast time e.g. 000 indicates the analysis step while 009 indicates a 9 hour
forecast.
* Once selected you can either press the “Submit” button or one of the time
forward or back arrows to load an image.
* There are 3 different annotation methods available with MARTIN. These are
Overlays, stamps and pen.

<hr>

# Contributing #

* A full guide on submitting issue and bug are given in our [contribution guidelines](https://github.com/cemac/MARTIN/blob/master/CONTRIBUTING.md)
* Please use our issue templates for feature requests and bug fixes.

## Developers

Please see [docs/DEVELOPER_GUIDE.pdf](./docs/DEVELOPER_GUIDE.pdf) for information
for App Developers.


# License

This code is currently licensed under the [MIT license](https://choosealicense.com/licenses/mit/).

# Acknowledgements

Developed by [Alex Roberts](https://environment.leeds.ac.uk/see/staff/1508/dr-alexander-roberts)
