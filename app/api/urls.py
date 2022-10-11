from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
# router.register('primary-property', views.PrimaryPropertyViewSet)

router = DefaultRouter()
router.register('api', views.ResalePropertyViewSet)

router = DefaultRouter()
router.register('api1', views.PrimaryPropertyViewSet)

urlpatterns = [
]