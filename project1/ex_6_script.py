"""
# cron running this script every 30 seconds
# m h  dom mon dow   command
* * * * * /usr/bin/python3.12 /home/jarek/PycharmProjects/SekurakPython/project1/ex_6_script.py
* * * * * sleep 30; /usr/bin/python3.12 /home/jarek/PycharmProjects/SekurakPython/project1/ex_6_script.py
"""

from datetime import datetime
import os
import sys

# current directory
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

# log test file for script
FILE = script_directory + "/script_test.txt"

now = datetime.now()

# write formatted date to log test file
with open (FILE, "a") as log:
    formatted = now.strftime("%A, %d %B %Y, %H:%M:%S")
    print("Formatted: ", formatted)
    log.write(f'{formatted}\n')