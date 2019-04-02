import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os


class Toolbar(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        self.menubar = tk.Menu(self, bg="lightgrey", fg="black")
        # FILE
        self.file_menu = tk.Menu(
            self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(
            label="Source", command=self.file_new_source)
        self.file_menu.add_command(
            label="New Window", command=self.file_new_window)
        self.file_menu.add_command(
            label="Save", command=self.file_save, accelerator="Ctrl+S")
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        # EDIT
        self.edit_menu = tk.Menu(
            self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.edit_menu.add_command(
            label="Clear notes", command=self.edit_cut)
        self.edit_menu.add_command(
            label="Clean background", command=self.edit_paste)
        self.edit_menu.add_command(
            label="Undo", command=self.edit_undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(
            label="Redo", command=self.edit_redo, accelerator="Ctrl+Y")
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        # View
        self.view_menu = tk.Menu(
            self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.view_menu.add_command(
            label="1-panel", command=self.panel_new)
        self.view_menu.add_command(
            label="2-panel", command=self.panel_split)
        self.menubar.add_cascade(label="View", menu=self.view_menu)
        # HELP
        self.help_menu = tk.Menu(
            self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.master.configure(menu=self.menubar)
        self.master.configure(menu=self.menubar)
        # Bind Options
        self.bind("<Control-s>", self.file_save)
        self.bind("<Control-n>", self.file_new_window)
        self.bind("<Control-v>", self.edit_paste)

    def file_new_window(self, event=None):
        return "break"

    def file_new_source(self, event=None):
        """
        Called when users press the 'Browse' button in order to choose a path on their system.
        """
        cwd = os.getcwd()
        new_path = None
        new_path = filedialog.askdirectory(title=self.master.title,
                                           initialdir=os.path.dirname(cwd),
                                           mustexist=True,
                                           parent=self.master)

        # Updates the text in the Entry with the new path name.
        if new_path:
            self.master.source_dir.set(new_path)

        return self.master.source_dir.set(new_path)

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

    def panel_new(self, event=None):
        return "break"

    def panel_split(self, event=None):
        return "break"

    def on_key_release(self, event):
        if not event.keysym in ("Up", "Down", "Left", "Right", "BackSpace", "Delete", "Escape"):
            self.display_autocomplete_menu()
