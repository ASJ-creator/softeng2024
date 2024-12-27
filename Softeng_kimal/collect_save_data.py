import DHTsensor, distance
import csv, time
from datetime import datetime
import os

def save_record(temp, hum, VPD, height):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    write_header = not os.path.exists(FILENAME)

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)

        if write_header:
            writer.writerow(["date", "temp", "hum", "VPD", "height"])

        writer.writerow([date, temp, hum, VPD, height])

FILENAME = "plant_record.csv"
times = 10

for i in range(times):
    t, h, v = DHTsensor.get_temp_hum_VPD()
    height = distance.get_distance()
    save_record(t,h,v,height)
    print(f"\r{i+1}/{times}", end="")
    time.sleep(1)