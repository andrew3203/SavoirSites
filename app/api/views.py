from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from api import serializers
from primary.models import PrimaryProperty
from resale.models import ResaleProperty
from aproperty.models import Client
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from django.contrib.sites.shortcuts import get_current_site
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from api.utils import get_html_msg, get_text_msg
from rest_framework.permissions import IsAuthenticated


class PropertyBase(generics.ListAPIView):
    search_fields = ['name','area__name']
    filter_backends = [
        filters.SearchFilter, 
        DjangoFilterBackend,
        filters.OrderingFilter, 
    ]
    filterset_fields = ['area__name',]


class PrimaryPropertyListView(PropertyBase):
    serializer_class = serializers.PrimaryMainSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        site = get_current_site(self.request)
        queryset = PrimaryProperty.objects.filter(site__site=site, is_published=True)
        return queryset


class ResalePropertyListView(PropertyBase):
    serializer_class = serializers.ResaleMainSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        site = get_current_site(self.request)
        queryset = ResaleProperty.objects.filter(site__site=site, is_published=True)
        return queryset


class PrimaryPropertyAPIView(generics.CreateAPIView):
    serializer_class = serializers.PrimaryPropertySerializer
    queryset = PrimaryProperty.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]


class ResalePropertyAPIView(generics.CreateAPIView):
    serializer_class = serializers.ResalePropertySerializer
    queryset = ResaleProperty.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()
        try:
            send_mail(
                subject=f'Новый контакт {contact.site}', 
                message=get_text_msg(contact),
                html_message=get_text_msg(contact),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=settings.RECIPIENT_ADDRESS,
            )
        except Exception as e:
            pass
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

