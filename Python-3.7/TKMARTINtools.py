# Set resource path to update based on whether code is being run as a python
# script or compiled to an executable.
# Once compiled the required imagery is included in the build and
# do not need seperate paths.

import os
import sys

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./resources/.")

    return os.path.join(base_path, relative_path)

# Function to flatten multidimensional lists.


def flat(alist):
    new_list = []
    for item in alist:
        if isinstance(item, (list, tuple)):
            new_list.extend(flat(item))
        else:
            new_list.append(item)
    return new_list
