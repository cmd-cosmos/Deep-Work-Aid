#pylint: skip-file
#type: ignore

import time
import os
import psutil
from enum import Enum

job_list = []
distractions = ["chrome.exe", "Chrome.exe", "brave.exe"]


class Job_Nature(Enum):
    WORK = 0
    DISTRACTION = 1

class Job:
    def __init__(self,id, type, time) -> None:
        self.id = id
        self.type = type
        self.time = time
    
    def categorize(self):
        if self.type == Job_Nature.DISTRACTION:
            print("Distracting Process Detected")
            job_list.append(id)
        elif self.type == Job_Nature.WORK:
            print("Setting as target job.")


for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] in distractions:
        print("Found")
        proc.terminate()

time.sleep(5)

path = os.path.join(".", "get_tabs.py")
os.system(f"python -u {path}")

