from gpiozero import DistanceSensor
from time import sleep

def get_distance():
    sensor = DistanceSensor(echo=19, trigger=20)
    return sensor.distance*100

def main():
    while True:
        print(get_distance())
        sleep(1)

if __name__ == "__main__":
    main()