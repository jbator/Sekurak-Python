import sys
import os
from pathlib import Path as pathlib_path


# read directory from program first argument
if len(sys.argv) != 2:
    sys.exit("Usage: python3 ex1_dir_files_printer.py <path>")

path = sys.argv[1]

# read program directory listing type (number
print("Select version or listing\n1: os.walk\n2: pathlib.Path\n3: recursive")
print("Enter number:")
try:
    version = int(input())
    if version < 1 or version > 3:
        raise ValueError("Wrong listing type number")
except ValueError:
    sys.exit("Wrong listing type number")

print(f"Listing all files from {path} - version {version}\n")

def list_files_1(directory):
    for root, dirs, files in os.walk(directory):
        print(f"{root} ({len(dirs)} dirs, {len(files)} files)")
        for file in files:
            print(' '*2,f"{file}")

def list_files_2(directory):
    for file in pathlib_path(directory).rglob('*'):
        print(f"{file}")

def list_files_3(directory, level):
    # local function variables
    #print(locals())
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)

        is_dir = os.path.isdir(full_path)
        file_info = (' ' * 2 * level) + file + (' (dir)' if is_dir else ' (file)')

        print(f"{file_info}")
        if is_dir:
            list_files_3(full_path, level+1)

# do listing based on type
if version == 1:
    list_files_1(path)
if version == 2:
    list_files_2(path)
if version == 3:
    list_files_3(path, 0)