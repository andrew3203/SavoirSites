from rest_framework import serializers


class LivingTypeSerializer(serializers.Serializer):
    name = serializers.CharField()


class ImageSerializer(serializers.Serializer):
    photo = serializers.ImageField()


class PropertySerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
    url = serializers.CharField()
    slug = serializers.SlugField()
    price = serializers.CharField()
    area = serializers.CharField()
    decor = serializers.CharField()
    rooms_number = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    title_image = serializers.ImageField()
    click_amount = serializers.IntegerField()
    living_type = LivingTypeSerializer(read_only=True, many=True)


class PrimaryPropertySerializer(PropertySerializer):
    presentation = serializers.FileField()
    logo = serializers.FileField()
    min_square = serializers.IntegerField()
    price_from = serializers.CharField()
  

class AreaSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
    url = serializers.CharField()
    slug = serializers.SlugField()