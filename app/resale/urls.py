from django.urls import path
from resale import views



urlpatterns = [
    path('<slug:slug>/', views.index, name='resale'),
]
