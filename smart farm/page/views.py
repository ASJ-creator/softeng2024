from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'page/home.html')

from django.views.generic import TemplateView
from django.http import StreamingHttpResponse, JsonResponse
from django.views import View
from django.core.cache import cache
import json
import queue
from .models import RFIDLog


class HomeView(TemplateView):
    template_name = 'page/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 최근 알림 5개를 컨텍스트에 추가
        context['recent_notifications'] = RFIDLog.objects.all()[:5]
        return context


class SSEView(View):
    def get(self, request, *args, **kwargs):
        def event_stream():
            client_queue = queue.Queue()
            clients = cache.get('sse_clients', [])
            clients.append(client_queue)
            cache.set('sse_clients', clients)

            try:
                while True:
                    message = client_queue.get()
                    yield f"data: {json.dumps(message)}\n\n"
            except:
                clients.remove(client_queue)
                cache.set('sse_clients', clients)

        response = StreamingHttpResponse(
            event_stream(),
            content_type='text/event-stream'
        )
        response['Cache-Control'] = 'no-cache'
        response['X-Accel-Buffering'] = 'no'
        return response


class RFIDNotificationView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        message = data.get('message', '')

        # 새로운 RFID 로그 생성
        RFIDLog.objects.create(message=message)

        return JsonResponse({'status': 'success'})



