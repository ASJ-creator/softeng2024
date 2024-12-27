#!/usr/bin/env python3

from picamera2 import Picamera2, Preview
from gpiozero import LED, Button
import time
import os

def takephoto(file_name):
    user = os.getlogin()
    user_home = os.path.expanduser(f'~{user}')
    camera = Picamera2()
    camera.start()
    camera.capture_file(f'{user_home}/{file_name}.jpg')


def main():
    # Get the current user's login name and home directory
    user = os.getlogin()
    user_home = os.path.expanduser(f'~{user}')
    print(user_home)
    # Initialize the camera
    camera = Picamera2()
    camera.start()

    # Initialize a variable to track the camera's status
    global status
    status = False

    # Set up LED and button with their GPIO pin numbers
    button = Button(21)

    def takePhotos(pin):
        """Function to set the camera's status to True when the button is pressed."""
        global status
        status = True

    try:
        # Assign the function to be called when the button is pressed
        button.when_pressed = takePhotos
        
        # Main loop
        while True:
            # Check if the button has been pressed
            if status:
                # Capture and save a photo
                camera.capture_file(f'{user_home}/my_photo.jpg')
                print('Take a photo!')          
                # Reset the status
                status = False
            else:
                # Turn off the LED if not capturing
                pass
            
            # Wait for a short period before checking the button status again
            time.sleep(1)

    except KeyboardInterrupt:
        # Stop the camera and turn off the LED if a KeyboardInterrupt occurs
        camera.stop_preview()
        pass
    
if __name__ == "__main__":
    main()