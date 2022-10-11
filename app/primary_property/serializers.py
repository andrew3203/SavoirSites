from rest_framework import serializers
from . import models



class PrimaryPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PrimaryProperty
        fields = '__all__'
        depth = 1
        
