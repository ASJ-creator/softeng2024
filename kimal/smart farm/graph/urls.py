from django.urls import path
from . import views
from .views import GraphView, DataUpdateView

app_name = 'graph'

urlpatterns = [
     path('', views.GraphView.as_view(), name='graph'),
     path('/update-data/', views.DataUpdateView.as_view(), name='update'),
]