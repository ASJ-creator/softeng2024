from django.shortcuts import render

# Create your views here.
def real_time_video(request):
    return render(request, 'video/video.html')

# 카메라
import cv2
from django.shortcuts import render
from django.http import StreamingHttpResponse

def video_feed(request):
    # OpenCV를 이용하여 카메라에서 영상 캡처
    cap = cv2.VideoCapture(0)

    def generate_frame():
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # 영상 프레임을 JPEG 형식으로 변환
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return StreamingHttpResponse(generate_frame(),
                                content_type='multipart/x-mixed-replace; boundary=frame')