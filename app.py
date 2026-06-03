import sounddevice as sd
import numpy as np
import time
import os
import webbrowser

# -----------------------------
# SETTINGS
# -----------------------------

THRESHOLD = 1.0          # Clap sensitivity
DOUBLE_CLAP_TIME = 1.0   # Seconds between claps
COOLDOWN = 10            # Prevent repeated triggers

# -----------------------------
# VARIABLES
# -----------------------------

last_clap_time = 0
clap_count = 0
last_trigger_time = 0

# -----------------------------
# WORKSPACE ACTIONS
# -----------------------------

def launch_workspace():
    print("Launching workspace...")

    # Open websites
    webbrowser.open("https://chatgpt.com")
    webbrowser.open("https://github.com")

    # Open Chrome
    os.system("start chrome")

    # Open VS Code
    os.system("start code")

    print("Workspace launched successfully!")

# -----------------------------
# AUDIO CALLBACK
# -----------------------------

def callback(indata, frames, time_info, status):

    global last_clap_time
    global clap_count
    global last_trigger_time

    volume = np.linalg.norm(indata)

    if volume > THRESHOLD:

        current_time = time.time()

        if current_time - last_clap_time < DOUBLE_CLAP_TIME:
            clap_count += 1
        else:
            clap_count = 1

        last_clap_time = current_time

        print(f"Clap count: {clap_count}")

        if clap_count == 2:

            if current_time - last_trigger_time > COOLDOWN:

                print("DOUBLE CLAP DETECTED!")

                launch_workspace()

                last_trigger_time = current_time

            clap_count = 0

# -----------------------------
# MAIN
# -----------------------------

print("Listening for double claps...")
print("Press CTRL + C to stop.")

try:
    with sd.InputStream(callback=callback):
        while True:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram stopped.")