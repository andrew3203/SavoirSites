from primary import models
from primary import serializers 
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PrimaryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = models.PrimaryProperty.objects.all()
    serializer_class = serializers.PrimarySerializer