from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose, name='choose'),
]