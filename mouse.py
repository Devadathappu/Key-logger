from pynput.mouse import Listener  # Import Listener from pynput.mouse

def writetofile(x, y):
    print('Position of mouse: {}'.format((x, y)))  # Corrected print statement

# Set up and start the listener for mouse movements
with Listener(on_move=writetofile) as l:  # Listens for mouse movements
    l.join()
