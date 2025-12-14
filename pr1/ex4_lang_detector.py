import sys
import os
import re
from pygments.lexers import guess_lexer

if len(sys.argv) != 2:
    sys.exit("Usage: python3 ex1_dir_files_printer.py <path>")

path = sys.argv[1]

if not os.path.isdir(path):
    sys.exit("Provide a valid directory path")

# languages data dict
PATTERNS = {
    'HTML': [r'\<\!DOCTYPE html>$', r'\<html', r'\<body', r'\<div'],
    'C/C++': [r'\#include', r'\#define'],
    'PHP': [r'\<\?php$'],
    'Python': [r'def +\:', r'import +']
}

KEYWORDS = {
    'HTML': ['<!DOCTYPE html>', '<html', '<body', '<div'],
    'C/C++': ['#include', '#define'],
    'PHP': ['<?php'],
    'Python': ['def ', 'import ']
}

# read user input method
def input_detecting_method():
    print("Select detecting lang method\n1: text in\n2: regex\n3: pygments")
    print("Enter number:")
    try:
        version = int(input())
        if version < 1 or version > 3:
            raise ValueError("Wrong method number")
        return version
    except ValueError as exception:
        sys.exit(str(exception))

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

def detect_lang_regex(file_path):
    try:
        with open(file_path) as f:
            for line in f.readlines():
                for language, patterns in PATTERNS.items():
                    for pattern in patterns:
                        match = re.match(pattern, line)
                        if match:
                            return language
    except UnicodeDecodeError:
        pass
    return None

def detect_lang_pygments(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            # read file content into var
            data = f.read()
            lang_detected = guess_lexer(data).name
            return lang_detected
    except UnicodeDecodeError:
        pass
    return None

method = input_detecting_method()

# detected languages
languages = set()

# loop over given path and detect language in text files
for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        is_dir = os.path.isdir(full_path)
        if not is_dir:
            match method:
                case 2:
                    lang = detect_lang_regex(full_path)
                case 3:
                    lang = detect_lang_pygments(full_path)
                case _:
                    lang = detect_lang(full_path)
            if lang and not lang in languages:
                print(f"Detected language: {lang} ({full_path})")
                languages.add(lang)

if len(languages) == 0:
    print("No languages detected")