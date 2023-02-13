from aproperty.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from resale.selectors import *
from resale import models
from django.shortcuts import render, get_object_or_404
from aproperty.models import SiteData
from django.contrib.sites.shortcuts import get_current_site



def index(request, slug):
    s = SiteData.objects.get(site=get_current_site(request))
    obj = get_object_or_404(models.ResaleProperty, slug=slug, site=s, is_published=True)
    obj.click_amount += 1; obj.save()
    context = {'obj': obj, 'site': s, 'site_id': s.site.pk, 'en': s.is_en()}
    return render(request, f'resale/index.html', context)


class ResaleListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = resaleList_get(**request.query_params)
        serializer = PropertySerializer(data, many=True)
        return Response(serializer.data)


class ResaleRecomendListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = resaleRecomend_get(**request.query_params)
        serializer = PropertySerializer(data, many=True)
        return Response(serializer.data)


class ResaleDetailApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        living_type = LivingTypeSerializer(many=True)
        images = ImageSerializer(many=True)

        class Meta:
            model = models.ResaleProperty
            exclude = ['site']
            depth = 1

    def get(self, request, id):
        data = resale_get(id=id)

        serializer = self.OutputSerializer(data)

        return Response(serializer.data)