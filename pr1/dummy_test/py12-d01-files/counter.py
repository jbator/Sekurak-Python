import os
from pprint import pprint
from collections import defaultdict
import time
from datetime import datetime
import json

SCRIPT_DIR = os.path.dirname(__file__)
# f"{SCRIPT_DIR}/random-stuff-master"

CODE_PATH = "/home/gynvael/code/HexArcana/course-python-10/project1/demo-nov/random-stuff-master"
COUNT_INTERVAL = 60  # Seconds.


LANG_PYTHON = "Python"
LANG_C_CPP = "C/C++"

KNOWN_EXT = {
  ".py": LANG_PYTHON,
  ".pyw": LANG_PYTHON,
  ".bat": "Batch",
  ".cmd": "Batch",
  ".c": LANG_C_CPP,
  ".h": LANG_C_CPP,
  ".hpp": LANG_C_CPP,
  ".cpp": LANG_C_CPP,
  ".cc": LANG_C_CPP,
  ".ino": LANG_C_CPP,
  ".php": "PHP",
  ".php3": "PHP",
  ".php4": "PHP",
  ".php5": "PHP",
  ".pl": "Perl",
  ".html": "HTML",
  ".htm": "HTML",
  ".js": "JavaScript",
  ".ts": "TypeScript",
  ".cs": "C#",
  ".java": "Java",
  ".kt": "Kotlin",
  ".sh": "Shell/Bash",
  ".rs": "Rust",
  ".rb": "Ruby",
  ".yml": "YAML",
  ".yaml": "YAML",
  ".ps1": "Powershell",
  ".s": "Assembly",
  ".asm": "Assembly",
  ".as": "Assembly",
  ".mk": "Makefile",
}

def detect_lang(fpath):
  _, ext = os.path.splitext(fpath)
  # .py
  # .PY
  # .Py
  ext = ext.lower()

  #if ext in KNOWN_EXT:
  #  return KNOWN_EXT[ext]
  lang = KNOWN_EXT.get(ext)
  if lang is not None:
    return lang

  fname = os.path.basename(fpath).lower()
  if fname == "makefile" or fname.startswith("makefile."):
    return "Makefile"

  return None

def count_loc(fpath, lang):
  with open(fpath, encoding="ibm437") as f:
    data = f.read()

  #lines = [
  #  line for line in data.splitlines() if line.strip() != ""
  #]
  loc = 0

  for line in data.splitlines():
    # "     asdf   "
    line = line.strip()   # "asdf"
    if line == "":
      continue

    if lang == LANG_PYTHON:
      if line.startswith("#"):
        continue
    elif lang == LANG_C_CPP:
      if line.startswith("//"):
        continue

    loc += 1

  #return len(lines)
  return loc


#stats = {}
def count_locs_in_path(code_path):
  now = datetime.now()
  stats = defaultdict(int)
  total_loc = 0
  for path, dirs, files in os.walk(code_path):
    for fname in files:
      fpath = f"{path}/{fname}"
      lang = detect_lang(fpath)

      if lang is None:
        continue

      loc = count_loc(fpath, lang)
      stats[lang] += loc
      #stats[lang] = stats[lang] + loc

      #if lang in stats:
      #  stats[lang] += loc
      #else:
      #  stats[lang] = loc

      total_loc += loc

  date = now.strftime("%Y-%m-%d %H:%M")
  #print("-" * 70, date)
  #pprint(dict(stats))
  #print(f"Total: {total_loc}")
  return {
    "date": date,
    "total": total_loc,
    "stats": dict(stats)
  }

stats_fpath = f"{SCRIPT_DIR}/stats.json"

try:
  with open(stats_fpath) as f:
    stats = json.load(f)
except FileNotFoundError:
  stats = []

while True:
  print("Counting...")
  loc = count_locs_in_path(CODE_PATH)
  stats.append(loc)

  with open(stats_fpath, "w") as f:
    json.dump(stats, f, indent=2)
  # f.__exit__()

  pprint(loc)
  time.sleep(COUNT_INTERVAL)


