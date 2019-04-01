# DEVELOPER GUIDE #

:+1::tada: Thanks for being interested in contributing or developing this tool further :tada::+1:

Please read [CONTRIBUTING.md](../CONTRIBUTING.md) for full contributing guides
for external Collaborators including.

## Requirements ##

* UNIX (Recommended)
* Anaconda Python 3 (Recommended)
* Packages (see Requirements.txt or MARTIN.yml

## Installation and Usage ##

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

Now changes can be made to `MARTIN.py`.

## Code alterations Python ##

*coming soon*

## Building standalone executables ##

*coming soon*

## Documentation Changes ##

*coming soon - suggest creating github.io docs page*

## TO DO ##

* Application improvements (listed in issues)
* Allow for alternate folder structure
* Make the application Pip installable
* FIX UNIX print screen bug
