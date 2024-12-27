from django.urls import path
from . import views

urlpatterns = [
    path('', views.control, name='control'),
    path('control/fetch-temperature-and-humidity/', views.fetch_temperature_and_humidity, name='fetch_temperature_and_humidity'),
    path('fetch-rfid-uid/', views.fetch_rfid_uid, name='fetch_rfid_uid'),
    path('control-servo-90/', views.control_servo_90, name='control_servo_90'),
    path('control-servo-180/', views.control_servo_180, name='control_servo_180'),
]