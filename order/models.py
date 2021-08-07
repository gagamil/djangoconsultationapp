from django.db import models

from client.models import Client
from specialist.models import Specialist


class Order(models.Model):
    STATUS_PENDING = 'STATUS_PENDING'
    STATUS_OK = 'STATUS_OK'
    STATUS_EXHAUSTED = 'STATUS_EXHAUSTED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_OK, 'Ok'),
        (STATUS_EXHAUSTED, 'Exhausted'),
    ]

    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    specialist = models.ForeignKey(Specialist, on_delete=models.PROTECT)

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_PENDING)
