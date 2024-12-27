from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_page, name='video_page'),
     path('video_feed/', views.video_feed, name='video_feed'),
    path('adjust_brightness/', views.adjust_brightness, name='adjust_brightness'),
    # path('adjust_white_balance/', views.adjust_white_balance, name='adjust_white_balance'),
]