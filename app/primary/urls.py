from primary import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', views.PrimaryViewSet, basename='primary')

urlpatterns = router.urls