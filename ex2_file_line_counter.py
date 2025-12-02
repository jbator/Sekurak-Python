import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: python3 ex2_file_lines_counter.py <path_to_py_file>")

path = sys.argv[1]

# check if file is dir
if os.path.isdir(path):
    sys.exit("File is directory")

# read all lines into local list
with open(path) as f:
    all_lines = f.readlines()

# count all lines
total_lines = len(all_lines)

# counters for type of lines
text_lines = 0
blank_lines = 0
comments_lines = 0

# loop over all lines and count types
for line in all_lines:
    # stip whitespaces from current line
    line = line.strip()

    # check if line is empty line
    if line == "":
        blank_lines += 1
    # check if lines is a python comment line
    elif line.startswith("#"):
        comments_lines += 1
    # regular text line
    else:
        text_lines += 1
        #print(f"Line: {line}")

print(f'Total lines: {total_lines}, Text lines: {text_lines}, Blank lines: {blank_lines}, Comments: {comments_lines}')