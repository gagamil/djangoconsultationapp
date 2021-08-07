from django.urls import include, path

from .views import OrderListCreateAPIView


urlpatterns = [
    path('', OrderListCreateAPIView.as_view(), name='new-order'),
]
