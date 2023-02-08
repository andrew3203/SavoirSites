from rest_framework import serializers
from primary.models import PrimaryProperty


class PrimarySerializer(serializers.ModelSerializer):
    price_from = serializers.CharField()

    class Meta:
        model = PrimaryProperty
        exclude = ['site']
        depth = 1




