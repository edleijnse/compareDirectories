# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import filecmp
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    dcmp = filecmp.dircmp('E:\Dropbox\Ger 2022-09-17 selektiert','E:\Dropbox\Ger 2022-09-17')
    print_diff_files(dcmp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
