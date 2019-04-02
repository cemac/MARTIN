# -*- coding: utf-8 -*-
"""
.. module:: MARTIN
    :platform: Unix/ Windows
    :synopis: Provide a user interface for navigating imagery for model
              data/case studies and allow users to annotate images and save.
              This has primarily been developed to assist in SWIFT testbeds,
              teaching and workshops.
.. moduleauthors: Alexander J. Roberts, (UoL, NCAS).
                  CEMAC (UoL).
.. description: This module was developed as part of
                Global Challenges Research Fund (GCRF) African SWIFT
                (Science for Weather Information and Forecasting Techniques.
   :copyright: © 2019 University of Leeds.
   :license: BSD-2 Clause.
Example:
    To use::
Memebers:
.. CEMAC_MARTIN:
   https://github.com/cemac/MARTIN
"""

import tkinter as tk
from tkinter import ttk
from toolbar import Toolbar
from navbar import Navbar
from main import Main
from statusbar import Statusbar


class MARTIN_App(ttk.Frame):
    """MARTIN_App
    args:
        self: class object
        master: parent object
    description:
        The wrapper for the app
    Memebers:
        toolbar = the top toolbar
        navbar = a side pannel
        statusbar = messages on app status
        main = the main image annotator
    """
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        # Bring in the various components
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)
        self.statusbar = Statusbar(self)
        # "Pack" them
        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        # Must put the "hero" widget in last
        self.main.pack(side="top", fill="both", expand=True)


# Main, calls app
if __name__ == '__main__':

    root = tk.Tk()
    app = MARTIN_App(root)
    app.mainloop()
