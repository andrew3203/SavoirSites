from rest_framework import viewsets
from api import serializers
from primary.models import PrimaryProperty
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class PrimaryPropertyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PrimaryPropertySerializer
    queryset = PrimaryProperty.objects.all()# .order_by('-click_amount')
    search_fields = ['name','area__name']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

