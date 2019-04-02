import tkinter as tk
from tkinter import ttk


class Statusbar(ttk.Frame):
    def __init__(self, master):
        """ Simple Status Bar class - based on Frame """
        super().__init__()
        self.master = master
        self.label = ttk.Label(self,anchor=tk.W)
        
    def set(self,texto):
        self.label.config(text=texto)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
