from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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