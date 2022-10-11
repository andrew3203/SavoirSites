from rest_framework import serializers
from . import models


class SpecialistSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Specialist
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Area
        fields = '__all__'


class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Click
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'
