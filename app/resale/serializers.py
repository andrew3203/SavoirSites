from rest_framework import serializers
from resale.models import ResaleProperty



class ResaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResaleProperty
        exclude = ['site']
        depth = 1

