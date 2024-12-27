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
    

def close_door(servo):
    servo.mid()
    

def main():
    from gpiozero import Servo
    from time import sleep

    servo = Servo(22)

    while True:
        servo.min()
        sleep(1)
        servo.mid()
        sleep(1)
        servo.max()
        sleep(1)

if __name__ == "__main__":
    main()