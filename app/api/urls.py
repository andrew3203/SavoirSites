from django.urls import path
from api import views



urlpatterns = [
    path('primary/', views.PrimaryPropertyListView.as_view()),
    path('resale/', views.ResalePropertyListView.as_view()),
    path('create-primary/', views.PrimaryPropertyAPIView.as_view()),
    path('create-resale/', views.ResalePropertyAPIView.as_view()),
    path('create-client/', views.ClientCreateAPIView.as_view()),
]