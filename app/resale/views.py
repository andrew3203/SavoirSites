from resale import models
from resale import serializers 
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ResaleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = models.ResaleProperty.objects.all()
    serializer_class = serializers.ResaleSerializer
    #permission_classes =[IsAuthenticated]
    #authentication_classes = [TokenAuthentication]