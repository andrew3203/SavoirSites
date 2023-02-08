from aproperty.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from primary.selectors import *
from primary import models



class PrimaryListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = primaryList_get(**request.query_params)
        serializer = PrimaryPropertySerializer(data, many=True)
        return Response(serializer.data)


class PrimaryRecomendListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = primaryRecomend_get(**request.query_params)
        serializer = PrimaryPropertySerializer(data, many=True)
        return Response(serializer.data)


class PrimaryDetailApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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