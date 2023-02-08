from django.urls import path
from aproperty import views



urlpatterns = [
    path('', views.index),
]