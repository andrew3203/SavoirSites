from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from primary_property import models, serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6

class PrimaryPropertyViewSet(viewsets.ModelViewSet):
    lookup_fields = ['pk', 'slug']
    serializer_class = serializers.PrimaryPropertySerializer
    queryset = models.PrimaryProperty.objects.all().order_by('-click_amount')
    #pagination_class = StandardResultsSetPagination


def index(request, slug):
    obj = get_object_or_404(models.PrimaryProperty, slug=slug)
    context = {'obj': obj}
    return render(request, 'primary_property/index.html', context)