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
import shutil

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def process_diff_files_left(dcmp, fromdirectory, todirectory, diffdirectory):
    dcmp = filecmp.dircmp(dcmp.left, dcmp.right)
    # print("left directory: %s" %(dcmp.left))
    # print("right direcory: %s" %(dcmp.right))

    left_only_files = sorted(dcmp.left_only)
    for name in left_only_files:
        if ("." in name):
           newdirectoryname = dcmp.left
           newdirectoryname = newdirectoryname.replace(fromdirectory,diffdirectory)

           print("left_only_file %s found in %s" % (name, dcmp.left) + " newdirectory: " + newdirectoryname)
           try:
               os.makedirs(newdirectoryname)
           # except FileExistError
           except OSError as e:
               dummy = 1
           oldfilename = dcmp.left + "/" + name
           newfilename = newdirectoryname + "/" + name
           shutil.copy(oldfilename,newfilename)
        else:
            print("left_only_directory %s found in %s" % (name, dcmp.left))
            # copy directory to target
            # Source path
            src = dcmp.left + "/" + name

            # Destination path
            dest = dcmp.left + "/" + name
            dest = dest.replace(fromdirectory,diffdirectory)
            # Copy the content of
            # source to destination
            destination = shutil.copytree(src, dest)
    for sub_dcmp in dcmp.subdirs.values():
        process_diff_files_left(sub_dcmp, fromdirectory, todirectory, diffdirectory)


class ConfigurateTaggerBiz(tk.Frame):

    def __init__(self, master=None):

        def open_directory(mydir, mytitle):
            """Open a file for editing."""

            dirpath = fd.askdirectory(initialdir=mydir, title=mytitle, parent=None)
            print(dirpath)

            if not dirpath:
                return
            return dirpath

        def compareFromClicked():
            print("compare from clicked")
            mydir = open_directory(self.filearray[0], "directory to compare from")
            btn_compare_from_dir_txt_var.set(mydir)
            self.filearray[0]=mydir

        def compareFromTextClicked():
            print("compare from text clicked")
            mydir = "this is the directory to compare from"
            tk.messagebox.showinfo("compare from directory", mydir)
            tk.Frame.__init__(self, master)
        def compareToClicked():
            print("compare to clicked")
            mydir = open_directory(self.filearray[0], "directory to compare to")
            btn_compare_to_dir_txt_var.set(mydir)
            self.filearray[1]=mydir
            save_file(self)

        def compareToTextClicked():
            print("compare to text clicked")
            mydir = "this is the directory to compare to"
            tk.messagebox.showinfo("compare to directory", mydir)
            tk.Frame.__init__(self, master)
            save_file(self)

        def compareResultClicked():
            print("compare result clicked")
            mydir = open_directory(self.filearray[2], "directory result")
            btn_compare_result_txt_var.set(mydir)
            self.filearray[2] = mydir
            save_file(self)

        def compareResultTextClicked():
            print("compare result clicked")
            mydir = "this is the directory to save the result"
            tk.messagebox.showinfo("compare result", mydir)
            tk.Frame.__init__(self, master)
            save_file(self)
        def compareStartClicked():
            print("compare start clicked")
            mydir = "start compare"
            tk.messagebox.showinfo("compare", mydir)
            tk.Frame.__init__(self, master)
            dcmp = filecmp.dircmp(self.filearray[0], self.filearray[1])
            process_diff_files_left(dcmp, self.filearray[0], self.filearray[1],self.filearray[2])
            mydir = "compare ended"
            tk.messagebox.showinfo("compare", mydir)

        def save_file(self):
            """Save the current file as a new file."""

            # filepath = fd.asksaveasfilename(
            #    defaultextension="txt",
            #    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            # )
            filepath = "compareDirectoriesconfig.txt"
            if not filepath:
                return
            with open(filepath, "w") as output_file:
                output_file.write(self.filearray[0] + "\n")
                output_file.write(self.filearray[1] + "\n")
                output_file.write(self.filearray[2] + "\n")
            output_file.close()

        def read_file(self):
            filepath = "compareDirectoriesconfig.txt"
            with open(filepath, "r") as input_file:
                ii = 0
                for x in input_file:
                    self.filearray[ii] = str(x).strip("\n")
                    ii = ii + 1
            input_file.close()

        self.grid
        self.filearray = ["", "", "", "", "", "", "", ""]
        read_file(self)
        self.fr_buttons = tk.Frame(master, relief=tk.RAISED, bd=2)
        self.btn_compare_from_dir = tk.Button(self.fr_buttons, text="COMPARE FROM directory",
                                              command=compareFromClicked, highlightbackground="cyan", bg="cyan")
        btn_compare_from_dir_txt_var = tk.StringVar()
        self.btn_compare_from_dir_txt = tk.Button(self.fr_buttons, textvariable=btn_compare_from_dir_txt_var,
                                                  command=compareFromTextClicked)
        btn_compare_from_dir_txt_var.set(self.filearray[0])
        self.btn_compare_from_dir.grid(row=0, column=0, sticky="ew", padx=5)
        self.btn_compare_from_dir_txt.grid(row=0, column=1, sticky="ew", padx=5)
        #
        self.btn_compare_to_dir = tk.Button(self.fr_buttons, text="COMPARE TO directory",
                                              command=compareToClicked, highlightbackground="cyan", bg="cyan")
        btn_compare_to_dir_txt_var = tk.StringVar()
        self.btn_compare_to_dir_txt = tk.Button(self.fr_buttons, textvariable=btn_compare_to_dir_txt_var,
                                                  command=compareToTextClicked)
        btn_compare_to_dir_txt_var.set(self.filearray[1])
        self.btn_compare_to_dir.grid(row=1, column=0, sticky="ew", padx=5)
        self.btn_compare_to_dir_txt.grid(row=1, column=1, sticky="ew", padx=5)
        #
        self.btn_compare_result_dir = tk.Button(self.fr_buttons, text="COMPARE result",
                                            command=compareResultClicked, highlightbackground="cyan", bg="cyan")
        btn_compare_result_txt_var = tk.StringVar()
        self.btn_compare_result_txt = tk.Button(self.fr_buttons, textvariable=btn_compare_result_txt_var,
                                                command=compareResultTextClicked)
        btn_compare_result_txt_var.set(self.filearray[2])
        self.btn_compare_result_dir.grid(row=2, column=0, sticky="ew", padx=5)
        self.btn_compare_result_txt.grid(row=2, column=1, sticky="ew", padx=5)
        #
        self.btn_compare_start = tk.Button(self.fr_buttons, text="start compare",
                                                command=compareStartClicked, highlightbackground="cyan", bg="cyan")
        self.btn_compare_start.grid(row=3, column=0, sticky="ew", padx=5)
        #
        self.fr_buttons.grid(row=0, column=0, sticky="ns")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("compare directories control centre")
    myConf = ConfigurateTaggerBiz(root)
    dirFrom = myConf.filearray[0]
    dirTo = myConf.filearray[1]
    # todo 20221023 button to start compare process
    root.mainloop()
    # dcmp = filecmp.dircmp(dirFrom, dirTo)
    # process_diff_files_left(dcmp)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
