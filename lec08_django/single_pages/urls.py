from django.urls import path
from . import views

app_name = "single_pages"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="careers"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
]