# Keylogger with Flask Server for File Upload

This project consists of a keylogger written in Python that captures keystrokes and sends the data to a Flask server for storage. The server appends the received data to a log file stored on a remote server (PythonAnywhere in this case).

## Features

- **Keylogger**: Captures user keystrokes in real-time.
- **File Upload**: Keystroke data is sent as a file to a Flask server.
- **Data Storage**: The Flask server receives and appends the captured keystrokes to a `log.txt` file stored in a remote server folder.
- **Real-time Updates**: The data is appended to the file whenever the keylogger captures new keystrokes.

## Technologies Used

- **Python**: Keylogger written in Python.
- **Flask**: Lightweight web framework used to create the server.
- **PythonAnywhere**: Web hosting platform for deploying the Flask server.
- **pynput**: Python library for capturing keystrokes.

## Setup and Installation

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/keylogger-flask.git
cd keylogger-flask
