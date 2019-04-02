# -*- coding: utf-8 -*-
"""
.. module:: Tk Modular system
    :platform: Unix/ Windows
    :synopis: A blank GUI
.. moduleauthors: Helen Burns - CEMAC (UoL).
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
from tkinter import colorchooser, filedialog, ttk


class Toolbar(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        self.FONT_SIZE = 12
        self.WINDOW_TITLE = "TEST"
        self.open_file = ""
        self.master.geometry("800x600")
        self.menubar = tk.Menu(self, bg="lightgrey", fg="black")
        self.file_menu = tk.Menu(
            self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(
            label="New", command=self.file_new, accelerator="Ctrl+N")
        self.file_menu.add_command(
            label="Open", command=self.file_open, accelerator="Ctrl+O")
        self.file_menu.add_command(
            label="Save", command=self.file_save, accelerator="Ctrl+S")
        self.edit_menu = tk.Menu(
            self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.edit_menu.add_command(
            label="Cut", command=self.edit_cut, accelerator="Ctrl+X")
        self.edit_menu.add_command(
            label="Paste", command=self.edit_paste, accelerator="Ctrl+V")
        self.edit_menu.add_command(
            label="Undo", command=self.edit_undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(
            label="Redo", command=self.edit_redo, accelerator="Ctrl+Y")
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.master.configure(menu=self.menubar)
        # Bind Options
        self.bind("<Control-s>", self.file_save)
        self.bind("<Control-o>", self.file_open)
        self.bind("<Control-n>", self.file_new)
        self.bind("<Control-v>", self.edit_paste)

    def file_new(self, event=None):
        file_name = filedialog.asksaveasfilename()
        if file_name:
            self.open_file = file_name
            self.title(" - ".join([self.WINDOW_TITLE, self.open_file]))

    def file_open(self, event=None):
        file_to_open = filedialog.askopenfilename()
        if file_to_open:
            self.open_file = file_to_open
        self.title(" - ".join([self.WINDOW_TITLE, self.open_file]))

    def file_save(self, event=None):
        if not self.open_file:
            new_file_name = filedialog.asksaveasfilename()
            if new_file_name:
                self.open_file = new_file_name

        if self.open_file:
            new_contents = 'have to set what sort of thing to save'
            with open(self.open_file, "w") as open_file:
                open_file.write(new_contents)

    def save_as(self, img):
        name = filedialog.asksaveasfilename(defaultextension=".png")
        if name:
            img.save(name)

    # exit program when window is closed
    def click_cancel(self, event=None):
        self.master.destroy()

    def edit_cut(self, event=None):
        self.event_generate("<<Cut>>")

        return "break"

    def edit_paste(self, event=None):
        self.event_generate("<<Paste>>")
        self.on_key_release()

        return "break"

    def edit_undo(self, event=None):
        self.event_generate("<<Undo>>")

        return "break"

    def edit_redo(self, event=None):
        self.event_generate("<<Redo>>")

        return "break"


class Navbar(ttk.Frame):
    def __init__(self, master):
        super().__init__()

    # exit program when window is closed
    def click_cancel(self, event=None):
        self.master.destroy()


class Statusbar(ttk.Frame):
    def __init__(self, master):
        super().__init__()


class Main(ttk.Frame):
    def __init__(self, master):
        super().__init__()


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)
        self.statusbar = Statusbar(self)
        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)


# Main, calls app
if __name__ == '__main__':

    root = tk.Tk()
    app = App(root)
    app.mainloop()
