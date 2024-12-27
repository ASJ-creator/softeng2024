from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
     path('', views.video_feed, name='video'),
     path('realtime/', views.real_time_video, name='realtime'),
]