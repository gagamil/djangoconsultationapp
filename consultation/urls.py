from django.urls import path

from .views import ConsultationListAPIView, ConsultationUpdateAPIView,\
    RoomConnectionTokenGetAPIView


urlpatterns = [
    path('', ConsultationListAPIView.as_view(), name='list-consultations'),
    path('<int:pk>/', ConsultationUpdateAPIView.as_view(), name='update-consultation'),
    path('<int:pk>/token/', RoomConnectionTokenGetAPIView.as_view(), name='get-rtc-token'),
]