#pylint: skip-file
#type: ignore

import time
import os
import psutil

distractions = ["chrome.exe", "Chrome.exe", "brave.exe"]

for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] in distractions:
        print("Found")
        proc.terminate()

time.sleep(5)

path = os.path.join(".", "get_tabs.py")
os.system(f"python -u {path}")

