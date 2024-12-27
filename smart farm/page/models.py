from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import json

# Create your models here.


class RFIDLog(models.Model):
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        # 알림이 저장될 때 연결된 모든 클라이언트에게 SSE로 전송
        super().save(*args, **kwargs)
        from django.core.cache import cache
        clients = cache.get('sse_clients', [])
        for client_queue in clients:
            client_queue.put({
                'type': 'notification',
                'message': self.message,
                'timestamp': self.timestamp.isoformat()
            })