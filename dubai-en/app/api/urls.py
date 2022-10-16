from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('primary', views.PrimaryPropertyViewSet)

urlpatterns = [
    path('create-client/', views.ClientCreateAPIView.as_view()),
    path('primary/', views.PrimaryPropertyListView.as_view()),
    path('', include(router.urls)),
]