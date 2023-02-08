from primary import views
from rest_framework import routers
from django.urls import path


urlpatterns = [
    path('', views.PrimaryListApi.as_view(), name='primary-list'),
    path('<int:id>/', views.PrimaryDetailApi.as_view(), name='primary-detail'),
    path('recomend/', views.PrimaryRecomendListApi.as_view(), name='primary-recomend'),
] 