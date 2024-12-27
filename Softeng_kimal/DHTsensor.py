import adafruit_dht as DHT
import board, time
from math import exp

def get_temp_hum_VPD(): # temp, hum, VPD
    dhtDevice = DHT.DHT11(board.D16)
    while True:
        try:
            temperature = round(dhtDevice.temperature, 2)
            humidity = round(dhtDevice.humidity, 2)
            SVP = 0.611 * exp((17.27*temperature) / (237.3+temperature))
            AVP = SVP * humidity/100
            VPD = round(SVP - AVP, 2)
            dhtDevice.exit()
            return temperature, humidity,VPD
        except:
            print("재시도")
            time.sleep(1)
            continue

def save_dht():
    pass


def main():
    try:
        data = get_temp_hum_VPD()
        print(data)

        temperature, humidity, VPD = get_temp_hum_VPD()
        if temperature is not None and humidity is not None:
            print(f"온도: {temperature}C, 습도: {humidity}%, VPD: {VPD}")
    except Exception as error:
        print(f"에러 발생: {error}")

if __name__ == "__main__":
    main()