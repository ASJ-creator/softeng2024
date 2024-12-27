from django.http import JsonResponse
from django.shortcuts import render
import json

def control_servo(request):
    if request.method == 'POST':
        try:
            # JSON ???? ??
            data = json.loads(request.body)
            angle = data.get('angle', 0)  # ????? 0 ??
            # ???? ??? ?? ??
            print(f"Received angle: {angle}")
            return JsonResponse({'message': 'Angle received', 'angle': angle}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def raspberry_control(request):
    return render(request, 'control/control.html')

# # GPIO 설정
# MOTOR_PIN = 18  # 사용하려는 GPIO 핀 번호
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(MOTOR_PIN, GPIO.OUT)


# def start_motor(request):
#     # 모터를 작동시키는 코드
#     GPIO.output(MOTOR_PIN, GPIO.HIGH)
#     return JsonResponse({"status": "Motor started"})

# def stop_motor(request):
#     # 모터를 정지시키는 코드
#     GPIO.output(MOTOR_PIN, GPIO.LOW)
#     return JsonResponse({"status": "Motor stopped"})


# def rotate_servo(angle):
#     import servo, time
#     servo_motor = servo.get_servo(22)
#     if angle==0:
#         pass
#         time.sleep(1)
#     elif angle==90:
#         status = servo.close_door(servo_motor)
#         print(status)
#         time.sleep(1)
#     elif angle==180:
#         servo.open_door(servo_motor)
#         time.sleep(1)
