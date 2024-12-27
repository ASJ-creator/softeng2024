#!/usr/bin/env python3
from gpiozero import Servo
from time import sleep

def get_servo(GPIO_num):
    myCorrection = 0.45
    maxPW = (2.0 + myCorrection) / 1000
    minPW = (1.0 - myCorrection) / 1000

    servo = Servo(GPIO_num, min_pulse_width=minPW, max_pulse_width=maxPW)
    return servo

def open_door(servo):
    servo.max()
    return 'Opening...'

def close_door(servo):
    servo.mid()
    return 'Closing...'

def main():
    try:
        servo = get_servo(22)

        while True:
            # Position the servo at the middle and wait
            open_door(servo)
            print("mid")  # Indicate current position
            sleep(0.5)    # Brief pause for 0.5 seconds

            # Move the servo to its maximum position and wait
            close_door(servo)
            print("max")  # Indicate current position
            sleep(1)      # Hold position for 1 second

    except KeyboardInterrupt:
        print("finished")
        pass

if __name__ == "__main__":
    main()