from rest_framework import viewsets, generics
from api import serializers
from primary.models import PrimaryProperty
from aproperty.models import Client
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend


class PrimaryPropertyListView(generics.ListAPIView):
    serializer_class = serializers.PrimaryMainSerializer
    queryset = PrimaryProperty.objects.all()
    search_fields = ['name','area__name']
    filter_backends = [
        filters.SearchFilter, 
        DjangoFilterBackend,
        filters.OrderingFilter, 
    ]
    filterset_fields = ['area__name', 'min_square', 'max_square']


class PrimaryPropertyAPIView(generics.CreateAPIView):
    serializer_class = serializers.PrimaryPropertySerializer
    queryset = PrimaryProperty.objects.all()

class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()

