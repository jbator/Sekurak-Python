import sys
import os

if len(sys.argv) != 2:
    sys.exit("Usage: python3 ex1_dir_files_printer.py <path>")

path = sys.argv[1]

if not os.path.isdir(path):
    sys.exit("Provide a valid directory path")

# languages data dict
KEYWORDS = {
    'HTML': ['<!DOCTYPE html>', '<html', '<body', '<div'],
    'C/C++': ['#include', '#define'],
    'PHP': ['<?php'],
    'Python': ['def ', 'import ']
}

# detector function
def detect_lang(file_path):
    lang_detected = None
    try:
        #print('File: ', file_path)
        with open(file_path, 'r', encoding="utf-8") as f:
            # read file content into var
            data = f.read()
            # loop over languages dict and its keywords to find any keyword
            for language, keywords in KEYWORDS.items():
                for keyword in keywords:
                    if keyword in data:
                        lang_detected = language
    except UnicodeDecodeError:
        pass
    return lang_detected

# detected languages
languages = set()

# loop over given path and detect language in text files
for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        is_dir = os.path.isdir(full_path)
        if not is_dir:
            lang = detect_lang(full_path)
            if lang and not lang in languages:
                print(f"Detected language: {lang} ({full_path})")
                languages.add(lang)

if len(languages) == 0:
    print("No languages detected")