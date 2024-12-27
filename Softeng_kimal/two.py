import sys
import termios
import tty
from picamera2 import Picamera2
import cv2

# ????? ? ?? ?? ??
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

# Picamera2 ?? ??
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

# ??? ??
picam2.start()

try:
    while True:
        # ??? ??
        frame = picam2.capture_array()

        # OpenCV? ??
        cv2.imshow("Frame", frame)

        # ? ?? ??
        if get_key() == 'q':
            break
finally:
    # ??? ??
    cv2.destroyAllWindows()
    picam2.stop()