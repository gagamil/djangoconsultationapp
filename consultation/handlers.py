from django.dispatch import receiver

from common.signals import order_cleared
from client.models import Client
from specialist.models import Specialist
from .models import Consultation


@receiver(order_cleared)
def handle_consultation_order_cleared(sender, **kwargs):
    client = Client.objects.get(pk=kwargs['client'])
    specialist = Specialist.objects.get(pk=kwargs['specialist'])
    Consultation.objects.create(client=client, specialist=specialist)
