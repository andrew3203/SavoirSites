from rest_framework import serializers
from . import models



class ResalePropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResaleProperty
        fields = '__all__'
