# MARTIN Application Code #

**Recommended Installation and usage method for Developers**

This is the Python code behind the MARTIN Image annotator code. This
application can be run directly as a python TK App.

## Requirements ##

* UNIX (Recommended)
* Anaconda Python 3 (Recommended)
* Packages (see Requirements.txt or MARTIN.yml)

## Installation and Usage (Recommended) ##

```bash
git clone https://github.com/cemac/MARTIN.git
cd MARTIN
conda create -f MARTIN.yml
cd MARTIN_IMAGE_ANNOTATIONS
ln -s ../Python-3.7/MARTIN.py .
ln -s ../resources .
# Add images in required structure (see user guide)
python MARTIN.py &
```

## Developers ##

Please refer [docs/DEVELOPER_GUIDE](../docs/DEVELOPER_GUIDE)
