from django.urls import path
from primary import views


urlpatterns = [
    path('', views.PrimaryListApi.as_view(), name='primary-list'),
    path('<int:id>/', views.PrimaryDetailApi.as_view(), name='primary-detail'),
    path('me/<slug:slug>/', views.index, name='my-primary'),
    path('recomend/', views.PrimaryRecomendListApi.as_view(), name='primary-recomend'),
] 