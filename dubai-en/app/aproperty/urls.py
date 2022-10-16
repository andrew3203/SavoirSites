from django.urls import path
from aproperty import views



urlpatterns = [
    path('', views.index),
    path('concierge/', views.concierge),
    path('privacy/', views.privacy),
]