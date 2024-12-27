
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

# === ??? ??? ?? ===
def get_temperature_and_humidity():
    from . import DHTsensor as dht
    t,h,v = dht.get_temp_hum_VPD()
    print(t,h,v)
    return t, h, v

def read_rfid_uid():
    from . import rfid
    uid = rfid.get_uid()
    return uid

def move_servo_motor(angle):
    from . import servo
    # servo_motor = servo.get_servo(22)
    if angle == 90:
        # servo_motor.mid()
        servo.Servo(22).mid()
        return f"Closed"
    elif angle == 180:
        # servo.open_door(servo_motor)
        servo.Servo(22).max()
        return f"Opened"

# === ? ?? ===
def control(request):
    return render(request, 'control/control.html')

def fetch_temperature_and_humidity(request):
    temperature, humidity, VPD = get_temperature_and_humidity()
    return JsonResponse({'message': f'Temperature: {temperature}C, Humidity: {humidity}%, VPD: {VPD}'})

def fetch_rfid_uid(request):
    from . import rfid
    from signal import pause
    uid = rfid.get_uid()
    pause()
    return JsonResponse({'message': f'RFID UID: {uid}'})

def control_servo_90(request):
    message = move_servo_motor(90)
    return JsonResponse({'message': message})

def control_servo_180(request):
    message = move_servo_motor(180)
    return JsonResponse({'message': message})