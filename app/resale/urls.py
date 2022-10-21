from django.urls import path
from primary import views



urlpatterns = [
    path('<slug:slug>/', views.index, name='resale'),
]
