#pylint: skip-file
#type: ignore

import subprocess

subprocess.Popen([
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "--remote-debugging-port=9222",
    r'--user-data-dir=C:\BraveDebug',
    "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgLLlzdgiTUKULKJPYc0A4q"
    ])

