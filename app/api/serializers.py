from rest_framework import serializers
from aproperty.models import Specialist, Area
from primary.models import PrimaryProperty, Image
from aproperty.models import Client


class PrimaryMainSerializer(serializers.ModelSerializer):
    url = serializers.CharField()
    price_from = serializers.CharField()
    squares = serializers.CharField()
    get_logo = serializers.CharField()

    class Meta:
        model = PrimaryProperty
        exclude = [
            'map_script', 'short_phrase', 'description', 'logo',
            'second_image', 'presentation', 'specialist', 'site'
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


