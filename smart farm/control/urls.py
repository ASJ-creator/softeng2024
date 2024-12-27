from django.urls import path
from . import views
# from .views import ServoControlView
app_name = 'control'

urlpatterns = [
    path('control/',views.raspberry_control, name='control'),
    # path('control/', ServoControlView.as_view(), name='servo-control'),
    # path('start/', views.start_motor, name='start_motor'),
    # path('stop/', views.stop_motor, name='stop_motor'),
    path('control/servo/', views.control_servo, name='control_servo'),
]