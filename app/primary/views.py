from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from primary.selectors import *


class LivingTypeSerializer(serializers.Serializer):
    name = serializers.CharField()

class ImageSerializer(serializers.Serializer):
   photo = serializers.ImageField()


class PrimaryListApi(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        id = serializers.IntegerField()
        url = serializers.CharField()
        slug = serializers.SlugField()
        price = serializers.IntegerField()
        price_from = serializers.CharField()
        area = serializers.CharField()
        decor = serializers.CharField()
        rooms_number = serializers.IntegerField()
        min_square = serializers.IntegerField()
        title_image = serializers.ImageField()
        logo = serializers.FileField()
        presentation = serializers.FileField()
        click_amount = serializers.IntegerField()
        living_type = LivingTypeSerializer(many=True)
        

    def get(self, request):
        data = primaryList_get(**request.query_params)
        serializer = self.OutputSerializer(data, many=True)
        return Response(serializer.data)


class PrimaryRecomendListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, site_domain):
        site = primaryRecomend_get(site_domain=site_domain, **request.query_params)

        serializer = serializers.PrimarySerializer(site, many=True)

        return Response(serializer.data)


class PrimaryDetailApi(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        living_type = LivingTypeSerializer(many=True)
        price_from = serializers.CharField()
        images = ImageSerializer(many=True)

        class Meta:
            model = models.PrimaryProperty
            exclude = ['site']
            depth = 1

    def get(self, request, id):
        data = primary_get(id=id)

        serializer = self.OutputSerializer(data)

        return Response(serializer.data)