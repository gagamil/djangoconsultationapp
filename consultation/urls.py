from django.urls import path

from .views import ConsultationListAPIView, ConsultationUpdateAPIView


urlpatterns = [
    path('', ConsultationListAPIView.as_view(), name='list-consultations'),
    path('<int:pk>/', ConsultationUpdateAPIView.as_view(), name='update-consultation'),
]