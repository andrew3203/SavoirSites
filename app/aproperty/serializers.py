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
    min_square = serializers.IntegerField()
    title_image = serializers.ImageField()
    logo = serializers.FileField()
    presentation = serializers.FileField()
    click_amount = serializers.IntegerField()
    living_type = LivingTypeSerializer(many=True)


class PrimaryPropertySerializer(PropertySerializer):
    price_from = serializers.CharField()
  