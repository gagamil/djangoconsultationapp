from rest_framework import generics
from rest_framework import views, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rtc.get_client_token import get_client_token
from .models import Consultation
from .serializers import ConsultationSerializer


class ConsultationListAPIView(generics.ListAPIView):
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Consultation.objects.filter(client__user=self.request.user)


class ConsultationUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Consultation.objects.filter(client__user=self.request.user)


class RoomConnectionTokenGetAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        consultation_id = pk
        queryset = Consultation.objects.filter(status__in=[Consultation.STATUS_PENDING, Consultation.STATUS_ACTIVE])
        consultation = get_object_or_404(queryset, pk=consultation_id)
        if not consultation.client.user == request.user and not consultation.specialist.user == request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        token = get_client_token(request.user.pk, consultation_id)
        return Response(token)