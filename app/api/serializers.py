from rest_framework import serializers
from aproperty.models import Specialist, Area, Image
from primary.models import PrimaryProperty
from aproperty.models import Client


class PrimaryMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrimaryProperty
        exclude = [
            'map_script', 'short_phrase', 'description', 
            'second_image', 'presentation', 'images', 'specialist'
        ]
        depth = 1

class PrimaryPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = PrimaryProperty
        fields = '__all__'
        depth = 1


class SpecialistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialist
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


