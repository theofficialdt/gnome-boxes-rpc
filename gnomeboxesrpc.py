#!/usr/bin/env python3
import time
import random
import subprocess
from pypresence import Presence

client_id = "1441064544234377369"
rpc = Presence(client_id)
rpc.connect()

activities = [
    ("Deleting /", 5),
    ("deleting system32", 5),
    ("editing a txt using nano", 60),
    ("Compiling the Linux Kernel", 45),
    ("Forgot sudo password", 14),
    ("Downloading more RAM", 8),
    ("Installing Arch Linux", 36),
    ("Trapped inside Vim", 50),
    ("Breaking the production database", 10),
    ("Updating Windows 98", 25),
    ("Mining bitcoin on CPU", 30)
]

process = subprocess.Popen(["gnome-boxes"])
start_timestamp = time.time()

try:
    while process.poll() is None:
        phrase, duration = random.choice(activities)
        rpc.update(
            state="Running QEMU/KVM with Gnome Boxes",
            details=phrase,
            start=start_timestamp
        )
        
        for _ in range(duration):
            if process.poll() is not None:
                break
            time.sleep(1)

except KeyboardInterrupt:
    process.terminate()

rpc.close()
