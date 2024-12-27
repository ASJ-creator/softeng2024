from gpiozero import Button            
from signal import pause
import rfid, servo, camera
from datetime import datetime

button = Button(21)             

# button.when_pressed = button_pressed

now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")


while True:
    if button.is_pressed == True:
        uid = rfid.get_uid()
        if uid == 'B5972902': # White Card
            serv = servo.get_servo(22)
            serv.max()
            break
        elif uid == 'F2EA4403': # Blue Chip
            serv = servo.get_servo(22)
            serv.mid()
            print("Access Denied")
            camera.takephoto(formatted_time)
            break