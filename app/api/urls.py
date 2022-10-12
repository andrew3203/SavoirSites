from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('primary', views.PrimaryPropertyViewSet)

urlpatterns = [
    path('', include(router.urls))
]