from rest_framework import serializers
from resale.models import ResaleProperty



class ResaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResaleProperty
        fields = '__all__'
        depth = 1

