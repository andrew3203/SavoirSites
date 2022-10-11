from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# router.register('primary-property', views.PrimaryPropertyViewSet)

urlpatterns = [
    path('', views.index),
    path('concierge/', views.concierge),
    path('privacy/', views.privacy),
]