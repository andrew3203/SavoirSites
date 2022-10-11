from django.shortcuts import render
from rest_framework import status, viewsets
from . import serializers
from . import models


class ResalePropertyViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ResalePropertySerializer
    queryset = models.ResaleProperty.objects.all()

