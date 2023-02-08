from django.urls import path
from resale import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'', views.ResaleViewSet, basename='resale')

urlpatterns = router.urls