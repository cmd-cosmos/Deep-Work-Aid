#pylint: skip-file
#type: ignore

import os
import subprocess

target_lectures = {
        "computer architecture" : "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgLLlzdgiTUKULKJPYc0A4q" 
}

target_readings = {
    "computer memory" : r"C:\Users\premt\OneDrive\Desktop\Programming Books and Notes\NOTES - AND - TEXTBOOKS\ESSENTIAL PAPERS\script.bat",


}

def brave_process_getter():
    subprocess.Popen([
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "--remote-debugging-port=9222",
        r'--user-data-dir=C:\BraveDebug',
        target_lectures["computer architecture"]
        ])

def pdf_process_getter():
    os.system(f"start {target_readings["computer memory"]}")

if __name__ == "__main__":
    brave_process_getter()
    pdf_process_getter()
