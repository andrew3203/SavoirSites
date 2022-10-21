from rest_framework import generics
from api import serializers
from primary.models import PrimaryProperty
from resale.models import ResaleProperty
from aproperty.models import Client
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from django.contrib.sites.shortcuts import get_current_site
from django_filters.rest_framework import DjangoFilterBackend


class PropertyBase(generics.ListAPIView):
    search_fields = ['name','area__name']
    filter_backends = [
        filters.SearchFilter, 
        DjangoFilterBackend,
        filters.OrderingFilter, 
    ]
    filterset_fields = ['area__name',]


class PrimaryPropertyListView(PropertyBase):
    serializer_class = serializers.PrimaryMainSerializer

    def get_queryset(self):
        site = get_current_site(self.request)
        queryset = PrimaryProperty.objects.filter(site__site=site, is_published=True)
        return queryset


class ResalePropertyListView(PropertyBase):
    serializer_class = serializers.ResaleMainSerializer

    def get_queryset(self):
        site = get_current_site(self.request)
        queryset = ResaleProperty.objects.filter(site__site=site, is_published=True)
        return queryset


class PrimaryPropertyAPIView(generics.CreateAPIView):
    serializer_class = serializers.PrimaryPropertySerializer
    queryset = PrimaryProperty.objects.all()
    permission_classes = [IsAdminUser]


class ResalePropertyAPIView(generics.CreateAPIView):
    serializer_class = serializers.ResalePropertySerializer
    queryset = ResaleProperty.objects.all()
    permission_classes = [IsAdminUser]


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()

