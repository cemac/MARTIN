import tkinter as tk
from tkinter import colorchooser, filedialog, ttk
import PIL.Image
import PIL.ImageTk
import PIL.ImageDraw
import platform
from statusbar import Statusbar
from TKMARTINtools_dev import flat, resource_path
plat = platform.system()
if plat == "Linux" or "Unix":
    import pyscreenshot as ImageGrab
else:
    import PIL.ImageGrab as ImageGrab


class Main(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        region_list = []
        init_list = []
        var_list = []
        region_count = 0
        init_count = 0
        var_count = 0
        self.pack(padx=5, pady=5)
        self.FONT_SIZE = 12
        self.master.title("MARTIN - Image Viewer")
        self.open_file = ""
        self.master.geometry("800x600")
        self.master.tk_setPalette(background='#ececec')
        self.master.protocol('WM_DELETE_WINDOW', self.click_cancel)
        self.master.bind('<Left>', self.previous)
        self.master.bind('<Right>', self.next)
        # Logo
        self.height = self.winfo_screenheight()
        logo_file = resource_path("MARTINlogo_small.png")
        self.logo = PIL.Image.open(logo_file)
        self.relogo = self.logo.resize((int(self.height * 0.15),
                                        int(self.height * 0.15)))
        self.tklogo = PIL.ImageTk.PhotoImage(self.relogo)
        self.logo_label = tk.Label(self, image=self.tklogo)
        self.logo_label.grid(row=1, column=0, rowspan=3)
        self.statusbar = Statusbar(self)
        self.statusbar.set("This is the statusbar")

    # Setup drawing on image
    def setup(self):
        self.draw_opt = "pen"
        self.old_x = None
        self.old_y = None
        self.line_width = self.thickness_button.get()
        self.color = "black"
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        self.linecount = 1

    # Update dropdown menus based on selection of source
    def update_source(self, *args):
        regions = sorted(list(self.fore_dict[self.var1.get()].keys()))
        menu = self.optionmenu2['menu']
        menu.delete(0, 'end')
        for region in regions:
            menu.add_command(
                label=region, command=lambda reg=region: self.var2.set(reg))

    # Update dropdown menus based on the region selected
    def update_region(self, *args):
        inits = sorted(
            list(self.fore_dict[self.var1.get()][self.var2.get()].keys()))
        menu = self.optionmenu3['menu']
        menu.delete(0, 'end')
        for init in inits:
            menu.add_command(label=init,
                             command=lambda ini=init: self.var3.set(ini))
        overlays = ["grid_black_" + self.var2.get(),
                    "grid_white_" + self.var2.get(),
                    "map_black_" + self.var2.get(),
                    "map_white_" + self.var2.get()]
        menu = self.optionmenu6['menu']
        menu.delete(0, 'end')

        for overlay in overlays:
            if glob.glob(resource_path(overlay + ".png")):
                menu.add_command(label=overlay,
                                 command=lambda over=overlay: self.var6.set(over))

    # Update dropdown menus based on the initiation selected
    def update_init(self, *args):
        varis = sorted(
            list(self.fore_dict[self.var1.get()][self.var2.get()][self.var3.get()].keys()))
        menu = self.optionmenu4['menu']
        menu.delete(0, 'end')
        for vari in varis:
            menu.add_command(label=vari,
                             command=lambda v=vari: self.var4.set(v))

    # Update dropdown menus based on the variable selected
    def update_var(self, *args):

        fores = self.fore_dict[self.var1.get(
        )][self.var2.get()][self.var3.get()][self.var4.get()]
        menu = self.optionmenu5['menu']
        menu.delete(0, 'end')
        for fore in fores:
            menu.add_command(
                label=fore, command=lambda f=fore: self.var5.set(f))

    # Check the values in the drop down menues are sensible on the use of the
    # submit button, advise on what needs changing or display image
    def check_vals(self, event=None):
        file_source = self.var1.get()
        file_region = self.var2.get()
        file_init = self.var3.get()
        file_var = self.var4.get()
        file_fore = self.var5.get()
        if file_fore == "000":
            file_name = glob.glob(file_source + "/" + file_region + "/" +
                                  file_init + "/" + file_var +
                                  "/*analysis*.png")[0]
        else:
            if(glob.glob(file_source + "/" + file_region + "/" + file_init +
                         "/" + file_var + "/*" + file_fore + ".png")):
                file_name = glob.glob(file_source + "/" + file_region + "/" +
                                      file_init + "/" + file_var + "/*" +
                                      file_fore + ".png")[0]
            else:
                file_name = ""
        print(file_name)

        if file_name:
            self.status['text'] = 'Annotate image as required'
        else:
            file_name = resource_path("No_image_loaded.png")
            self.status['text'] = 'Cannot find image please select other option'

        self.im = PIL.Image.open(file_name)
        aspect_ratio = self.im.size[0] / self.im.size[1]
        self.reim = self.im.resize((int(self.height * 0.666 * aspect_ratio),
                                   int(self.height * 0.666)))
        self.tkim = PIL.ImageTk.PhotoImage(self.reim)
        self.canvas.delete(self.tkim)
        self.canvas.create_image(self.height / 2 + 10, int(self.height *
                                                           0.666) / 2 + 10,
                                 image=self.tkim, tags="back")
        self.canvas.tag_raise("lines")

    # Check the values in the drop down menues are sensible on the use of the
    # submit button, advise on what needs changing or display image
    def check_overlay(self, *args):

        file_var = self.var6.get()

        ol_file_name = resource_path(file_var + ".png")

        self.olim = PIL.Image.open(ol_file_name)
        aspect_ratio = self.olim.size[0] / self.olim.size[1]
        self.olreim = self.olim.resize((int(self.height * 0.666 *
                                            aspect_ratio),
                                        int(self.height * 0.666)))

        globals()["oltkim%04d" %
                  self.linecount] = PIL.ImageTk.PhotoImage(self.olreim)
        self.canvas.create_image(self.height / 2 + 10,
                                 int(self.height * 0.666) / 2 + 10,
                                 image=globals()["oltkim%04d" % self.linecount],
                                 tags=("lines", "%04d" % self.linecount))
        self.linecount = self.linecount + 1

    # Set background image to previous time
    def previous(self, event=None):

        file_source = self.var1.get()
        file_region = self.var2.get()
        file_init = self.var3.get()
        file_var = self.var4.get()
        file_fore = self.var5.get()
        if file_fore == "":
            file_fore = self.fore_dict[file_source][file_region][file_init][file_var][0]
        if file_fore == self.fore_dict[file_source][file_region][file_init][file_var][0]:
            file_fore = self.fore_dict[file_source][file_region][file_init][file_var][0]
        else:
            file_fore = "%03d" % (int(file_fore) - 3)

    # Set background image to next time
    def next(self, event=None):

        file_source = self.var1.get()
        file_region = self.var2.get()
        file_init = self.var3.get()
        file_var = self.var4.get()
        file_fore = self.var5.get()

        if file_fore == "":
            file_fore = self.fore_dict[file_source][file_region][file_init][file_var][0]

        list_len = len(self.fore_dict[file_source]
                       [file_region][file_init][file_var])
        fore_pos = self.fore_dict[file_source][file_region][file_init][file_var].index(
            file_fore)
        if (fore_pos + 1 < list_len):
            file_fore = "%03d" % (int(file_fore) + 3)
        else:
            file_fore = self.fore_dict[file_source][file_region][file_init][file_var][list_len - 1]

# Keep for when satellite data is to be used

#      elif file_type == "GFS":
#         if file_time >= "048":
#            file_time = "048"
#         else:
#            file_time = "%03d" % (int(file_time)+3)
#      else:
#         if file_time >= "021":
#            list_len = len(self.date_dict[file_type][file_case][file_var])
#            date_pos = self.date_dict[file_type][file_case][file_var].index(file_date)
#            if(date_pos+1 < list_len):
#               file_time = "000"
#               file_date = self.date_dict[file_type][file_case][file_var][date_pos+1]
#               self.var4.set(file_date)
#         else:
#            file_time = "%03d" % (int(file_time)+3)

        self.var5.set(file_fore)
        self.check_vals()

    # Choose pen option
    def choose_pen(self):
        self.draw_opt = "pen"
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    # Choose stamp option
    def choose_stamp(self, img):
        self.draw_opt = "stamp"
        self.stamp_img = img
        self.canvas.bind('<Button-1>', self.stamp)

    # Paint smooth lines on canvas
    def paint(self, event):
        if self.draw_opt == "pen":
            paint_color = self.color
            self.line_width = self.thickness_button.get()
            if self.old_x and self.old_y:
                self.canvas.create_line(self.old_x, self.old_y, event.x,
                                        event.y, width=self.line_width,
                                        fill=paint_color, capstyle='round',
                                        smooth='true', splinesteps=36,
                                        tags=("lines",
                                              "%04d" % self.linecount))
            self.old_x = event.x
            self.old_y = event.y

    # Stamp image on canvas when clicked
    def stamp(self, event):
        if self.draw_opt == "stamp":
            self.canvas.create_image(event.x, event.y, image=self.stamp_img,
                                     tags=("lines", "%04d" % self.linecount))

    # Reset before next event
    def reset(self, event):
        self.linecount = self.linecount + 1
        self.old_x, self.old_y = None, None

    # Call the colour chooser and update paint colour
    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    # Undo the last line drawn
    def undo(self):
        if self.linecount >= 1:
            del_id = self.linecount - 1
            self.canvas.delete("%04d&&lines" % del_id)
            self.linecount = self.linecount - 1

    # Clear all lines drawn so far
    def clear(self):
        self.canvas.delete("lines")
        self.linecount = 1

    # Clear background image
    def clear_back(self):
        self.canvas.delete("back")

    # Grab all on current canvas
    def save_all_crop(self, canvas):
        x = root.winfo_rootx() + canvas.winfo_x() + 11
        y = root.winfo_rooty() + canvas.winfo_y() + 11
        x1 = x + canvas.winfo_width() - 23
        y1 = y + canvas.winfo_height() - 24
        self.grab_img = ImageGrab.grab(bbox=(x, y, x1, y1))
        self.check_img()

    # Check to see if grabbed canvas is black
    def check_img(self):
        if self.grab_img.getbbox() is None:
            self.save_all_crop(self.canvas)
        else:
            self.save_as(self.grab_img)

    def save_as(self, img):
        name = filedialog.asksaveasfilename(defaultextension=".png")
        if name:
            img.save(name)

    # exit program when window is closed
    def click_cancel(self, event=None):
        self.master.destroy()
