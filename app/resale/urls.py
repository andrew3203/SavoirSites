from resale import views
from rest_framework import routers
from django.urls import path


urlpatterns = [
    path('', views.ResaleListApi.as_view(), name='resale-list'),
    path('<int:id>/', views.ResaleDetailApi.as_view(), name='resale-detail'),
    path('recomend/', views.ResaleRecomendListApi.as_view(), name='resale-recomend'),
] 