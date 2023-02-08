from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from api import serializers
from aproperty.models import Client
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



def get_text_msg(contact):
    text = f"Новый контакт: {contact.site}" + "\n\n" \
        f"Имя: {contact.name}" + "\n\n"  \
        f"Телефон: {contact.phone}" + "\n\n"  \
        f"Почта: {contact.email}" + "\n\n"  \
        f"Объект: {contact.complex}" 
    return text



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

