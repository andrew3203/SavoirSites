from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from api import serializers
from primary.models import PrimaryProperty
from resale.models import ResaleProperty


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6


class PrimaryPropertyViewSet(viewsets.ModelViewSet):
    lookup_fields = ['pk', 'slug']
    serializer_class = serializers.PrimaryPropertySerializer
    queryset = PrimaryProperty.objects.all().order_by('-click_amount')
    #pagination_class = StandardResultsSetPagination


class ResalePropertyViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ResalePropertySerializer
    queryset = ResaleProperty.objects.all()
