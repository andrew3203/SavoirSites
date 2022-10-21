from rest_framework import serializers
from aproperty.models import Client
from primary.models import PrimaryProperty
from resale.models import ResaleProperty


class PrimaryMainSerializer(serializers.ModelSerializer):
    url = serializers.CharField()
    price_from = serializers.CharField()
    squares = serializers.CharField()
    get_logo = serializers.CharField()
    squares_en = serializers.CharField()
    price_from_en = serializers.CharField()

    class Meta:
        model = PrimaryProperty
        exclude = [
            'map_script', 'short_phrase', 'description', 'logo',
            'second_image', 'presentation', 'specialist', 'site'
        ]
        depth = 1


class ResaleMainSerializer(serializers.ModelSerializer):
    url = serializers.CharField()

    class Meta:
        model = ResaleProperty
        exclude = [
            'map_script', 'description', 'specialist', 'site'
        ]
        depth = 1


class PrimaryPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = PrimaryProperty
        fields = '__all__'
        depth = 1


class ResalePropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = ResaleProperty
        fields = '__all__'
        depth = 1


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
