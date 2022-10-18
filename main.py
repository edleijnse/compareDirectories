# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import filecmp
import tkinter as tk
import os
from tkinter import filedialog as fd, DISABLED
from tkinter import messagebox
from tkinter import simpledialog
from filecmp import dircmp

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_diff_files(dcmp):
    common_files = sorted(dcmp.common_files)
    for name in common_files:
        print("common_file %s found in %s and %s" % (name, dcmp.left,
              dcmp.right))
    left_only_files = sorted(dcmp.left_only)
    for name in left_only_files:
        print("left_only_file %s found in %s" % (name, dcmp.left))
    right_only_files = sorted(dcmp.right_only)
    for name in right_only_files:
        print("right_only_file %s found in %s " % (name, dcmp.left))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)


class ConfigurateTaggerBiz(tk.Frame):

    def __init__(self, master=None):
        def lightroomClicked():
           print("Lightroom clicked")
           mydir = open_directory(self.filearray[1], "YOUR Lightroom directory")
           btn_lightroom_dir_txt_var = tk.StringVar()
           btn_lightroom_dir_txt_var.set(mydir)
           self.directory_02_txt = mydir

        def lightroomTextClicked():
            print("LightroomText clicked")
            mydir = "this is the directory where you original Lightroom files are. Your MASTER directory!"
            tk.messagebox.showinfo("Lightroom directory", mydir)

        tk.Frame.__init__(self, master)
        self.grid
        self.filearray = ["", "", "", "", "", "", "", ""]
        self.fr_buttons = tk.Frame(master, relief=tk.RAISED, bd=2)
        self.btn_lightroom_dir = tk.Button(self.fr_buttons, text="YOUR Lightroom directory",
                                           command=lightroomClicked, highlightbackground="cyan", bg="cyan")
        btn_lightroom_dir_txt_var = tk.StringVar()
        self.btn_lightroom_dir_txt = tk.Button(self.fr_buttons, textvariable=btn_lightroom_dir_txt_var,
                                               command=lightroomTextClicked)
        btn_lightroom_dir_txt_var.set(self.filearray[1])
        self.btn_lightroom_dir.grid(row=0, column=0, sticky="ew", padx=5)
        self.btn_lightroom_dir_txt.grid(row=0, column=1, sticky="ew", padx=5)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")

        def open_directory(mydir, mytitle):
           """Open a file for editing."""

           dirpath = fd.askdirectory(initialdir=mydir, title=mytitle, parent=None)
           print(dirpath)

           if not dirpath:
              return
           return dirpath



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    dcmp = filecmp.dircmp('E:\Dropbox\Ger 2022-09-17 selektiert','E:\Dropbox\Ger 2022-09-17')
    print_diff_files(dcmp)
    root = tk.Tk()
    root.wm_title("compare directories control centre")
    myConf = ConfigurateTaggerBiz(root)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
