import tkinter as tk
from tkinter import ttk
from toolbar import Toolbar
from navbar import Navbar
from main import Main
from statusbar import Statusbar


class App(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)
        self.statusbar = Statusbar(ttk.Frame(master))
        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="top", fill="both", expand=True)

# Main, calls app
if __name__ == '__main__':

    root = tk.Tk()
    app = App(root)
    app.mainloop()
