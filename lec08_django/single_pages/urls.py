from django.urls import path
from . import views

app_name = "single_pages"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", views.index, name="index"),
    path("careers/", views.careers, name="careers"),
    path("contact/", views.contact, name="contact"),
]