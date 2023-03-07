import os
import sys
from PIL import Image
from pathlib import Path
import imghdr
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog

columns = {"file": "File:",
           "size": "Size(in px):",
           "dpi": "DPI:",
           "color_depth": "Color depth:",
           "compression": "Compression:"}

mode_to_bpp = {'1': 1,
               'L': 8,
               'P': 8,
               'RGB': 24,
               'RGBA': 32,
               'CMYK': 32,
               'YCbCr': 24,
               'I': 32,
               'F': 32}

tree: ttk.Treeview
menubar: tk.Menu

# function to bind the path for use with the packaged pyinstaller folders
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)

def inspect_folder():
    photos = []
    folder_path = filedialog.askdirectory(initialdir='.', title='Choose the folder:')

    menubar.entryconfigure(2, label="Folder (" + folder_path + ")")
    no_images = True
    for root_folder, _, files in os.walk(folder_path):
        for file in files:
            image_path = root_folder + '/' + file

            if imghdr.what(image_path) is None:
                continue

            image = Image.open(image_path)
            if not image.verify:
                continue

            photos.append((file, 'x'.join(map(str, image.size)), image.info.get('dpi'), mode_to_bpp[image.mode],
                           image.info.get('compression')))
            no_images = False

    if no_images:
        messagebox.showinfo(title="Info", message="No image files detected in '" + folder_path + "'")

    for item in tree.get_children():
        tree.delete(item)

    for image in photos:
        tree.insert("", tk.END, values=image)


def clear_table():
    menubar.entryconfigure(1, label="Folder")
    for item in tree.get_children():
        tree.delete(item)


def main():
    win = tk.Tk()
    win.iconbitmap(resource_path("pics/seo.ico"))
    win.title("Images info")
    win.geometry("1080x640")
    win.minsize(500, 500)

    global menubar
    menubar = tk.Menu(win, background='blue', font=font.Font(weight=font.BOLD))
    folder_menu = tk.Menu(menubar, tearoff=0)
    folder_menu.add_command(label='Inspect', command=inspect_folder)
    folder_menu.add_separator()
    folder_menu.add_command(label='Reset', command=clear_table)
    menubar.add_cascade(label='Folder', menu=folder_menu)

    win.config(menu=menubar)
    style = ttk.Style()
    style.theme_use('alt')
    style.configure("Treeview.Heading", font=font.Font(weight=font.BOLD))

    global tree
    tree = ttk.Treeview(columns=list(columns.keys()), show="headings")

    for key, value in columns.items():
        tree.heading(key, text=value, )

    for column in columns.keys():
        tree.column(column, anchor=tk.CENTER, stretch=tk.YES, width=100)

    tree.pack(fill=tk.BOTH, expand=1)

    win.mainloop()


if __name__ == '__main__':
    main()

# create executable single-file app
# pyinstaller --windowed -F --add-data "pics/seo.ico;pics" --icon=pics/seo.ico -d bootloader main.py --name inspect_images --onefile