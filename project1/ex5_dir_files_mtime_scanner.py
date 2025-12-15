import os
import sys
from time import sleep
from datetime import datetime
from watchdog.events import FileModifiedEvent, FileSystemEventHandler
from watchdog.observers import Observer

INTERVAL = 1

if len(sys.argv) != 2:
    sys.exit("Usage: python ex5_dir_files_mtime_scanner.py <path>")

path = sys.argv[1]

if not os.path.isdir(path):
    sys.exit("Provide a valid directory path")

print("Select scanning method: 1 - active polling | 2 - watchdog:\n")

try:
    version = int(input())
    if version < 1 or version > 3:
        raise ValueError("Wrong method number")
except ValueError as exception:
    sys.exit(str(exception))

cache = {}

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileModifiedEvent)->None:
        if event.event_type == 'modified' and not event.is_directory:
            #if isinstance(event, FileModifiedEvent) and not event.is_directory:
            stats = os.stat(event.src_path)
            print(event.src_path + ': ', stats.st_mtime)

# scan dir files for mtime changes using os walk and files stats checks
def active_polling(directory):
    while True:
        for root, dirs, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                is_dir = os.path.isdir(full_path)
                if not is_dir:
                    stats = os.stat(full_path)
                    last_modified = None
                    if full_path in cache:
                        last_modified = cache[full_path]
                    if last_modified != stats.st_mtime:
                        cache[full_path] = stats.st_mtime
                        modified = datetime.fromtimestamp(cache[full_path]).strftime('%Y-%m-%d %H:%M:%S')
                        print(file + ': ' + modified)

        sleep(INTERVAL)

def watchdog(directory):
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    try:
        while True:
            sleep(INTERVAL)
    finally:
        observer.stop()
        observer.join()


if version == 2:
    watchdog(path)
else:
    active_polling(path)