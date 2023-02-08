from aproperty.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from resale.selectors import *
from resale import models


class ResaleListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = resalList_get(**request.query_params)
        serializer = PropertySerializer(data, many=True)
        return Response(serializer.data)


class ResaleRecomendListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = resalRecomend_get(**request.query_params)
        serializer = PropertySerializer(data, many=True)
        return Response(serializer.data)


class ResaleDetailApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        living_type = LivingTypeSerializer(many=True)
        price_from = serializers.CharField()
        images = ImageSerializer(many=True)

        class Meta:
            model = models.ResaleProperty
            exclude = ['site']
            depth = 1

    def get(self, request, id):
        data = resale_get(id=id)

        serializer = self.OutputSerializer(data)

        return Response(serializer.data)