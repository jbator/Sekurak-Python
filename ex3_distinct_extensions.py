import sys
import os
from pprint import pprint

#read directory from program first argument
if len(sys.argv) != 2:
    sys.exit("Usage: python3 ex3_distinct_extensions.py <path>")

path = sys.argv[1]

if not os.path.isdir(path):
    sys.exit("Provide a valid directory path")

# default unique extensions set
extensions = set()

# check for files in directory
for path, dirs, files in os.walk(path):
    for file in files:
        # split file extension and rest of the path
        _, ext = os.path.splitext(file)
        # when extension is not empty add to unique set
        if ext != "":
            extensions.add(ext)

# print extensions
for ext in extensions:
    print(ext)