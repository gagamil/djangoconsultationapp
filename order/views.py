from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from common.signals import order_cleared
from .models import Order
from .serializers import OrderSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(client__user=self.request.user)

    def perform_create(self, serializer):
        client = self.request.user.client
        order = serializer.save(client=client)

        # Business rule in view method
        if order.specialist.price == 0:
            order.status = Order.STATUS_OK
            order.save()
            order_cleared.send(sender=self.__class__, specialist=order.specialist.pk, client=order.client.pk)
