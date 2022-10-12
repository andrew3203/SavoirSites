from rest_framework import viewsets, generics
from api import serializers
from primary.models import PrimaryProperty
from aproperty.models import Client
from rest_framework import filters
from rest_framework.permissions import IsAdminUser

class PrimaryPropertyListView(generics.ListAPIView):
    serializer_class = serializers.PrimaryMainSerializer
    queryset = PrimaryProperty.objects.all()
    search_fields = ['name','area__name']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

class PrimaryPropertyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PrimaryPropertySerializer
    queryset = PrimaryProperty.objects.all()
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        pass

class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()

