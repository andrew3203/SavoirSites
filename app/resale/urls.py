from django.urls import path
from resale import views


urlpatterns = [
    path('', views.ResaleListApi.as_view(), name='resale-list'),
    path('<int:id>/', views.ResaleDetailApi.as_view(), name='resale-detail'),
     path('me/<slug:slug>/', views.index, name='resale'),
    path('recomend/', views.ResaleRecomendListApi.as_view(), name='resale-recomend'),
] 