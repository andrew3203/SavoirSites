from django.urls import path
from api import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('primary/', views.PrimaryPropertyListView.as_view()),
    path('resale/', views.ResalePropertyListView.as_view()),
    path('create-primary/', views.PrimaryPropertyAPIView.as_view()),
    path('create-resale/', views.ResalePropertyAPIView.as_view()),
    path('create-client/', views.ClientCreateAPIView.as_view()),
]