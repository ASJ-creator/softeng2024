from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from picamera2 import Picamera2
import cv2


def video_page(request):
    return render(request, 'video/index.html')

from django.http import StreamingHttpResponse, JsonResponse
from picamera2 import Picamera2
import cv2
import threading

# Picamera2 ???
camera = Picamera2()
camera.configure(camera.create_video_configuration(main={"size": (640, 480)}))
camera.start()

# ??? ??
lock = threading.Lock()

# ?? ??? ??? ??? ??
brightness = 0
white_balance = 1.0

# ??? ?? ?? (RGB ?? ??)
def generate_frames():
    global brightness, white_balance
    while True:
        with lock:
            # ??? ?? ? ?? ??
            frame = camera.capture_array()
            frame = cv2.convertScaleAbs(frame, alpha=1, beta=brightness)  # ?? ??
            # RGB ??
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # JPEG ???
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        # ???? ??? ??
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# ??? ?? ??
def video_feed(request):
    return StreamingHttpResponse(generate_frames(),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

# ?? ??
def adjust_brightness(request):
    global brightness
    value = int(request.GET.get('value', 0))
    with lock:
        brightness = value - 50  # ???? ?(0~100)? -50~50 ??? ??
    return JsonResponse({"status": "ok"})

# ??? ??? ??
# def adjust_white_balance(request):
#     global white_balance
#     value = int(request.GET.get('value', 100))
#     with lock:
#         white_balance = value / 100.0  # ???? ?(0~100)? 0.0~1.0 ??? ??
#         camera.set_controls({"AwbMode": "Manual", "ColourGains": (white_balance, white_balance)})
#     return JsonResponse({"status": "ok"})