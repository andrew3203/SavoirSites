from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import serializers
from aproperty.models import Client, SiteData
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.selectors import *



def get_text_msg(contact):
    text = f"Новый контакт: {contact.site}" + "\n\n" \
        f"Имя: {contact.name}" + "\n\n"  \
        f"Телефон: {contact.phone}" + "\n\n"  \
        f"Почта: {contact.email}" + "\n\n"  \
        f"Объект: {contact.complex}" 
    return text



class ClientCreateAPIView(generics.CreateAPIView):
    class ClientSerializer(serializers.ModelSerializer):

        class Meta:
            model = Client
            fields = '__all__'

    serializer_class = ClientSerializer
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



class SiteDataApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = SiteData
            fields = '__all__'

    def get(self, request, site_domain):
        site = site_get(site_domain=site_domain)

        serializer = self.OutputSerializer(site)

        return Response(serializer.data)