from django.db import models

from client.models import Client
from specialist.models import Specialist


class Consultation(models.Model):
    STATUS_PENDING = 'STATUS_PENDING'
    STATUS_ACTIVE = 'STATUS_ACTIVE'
    STATUS_CANCELLED = 'STATUS_CANCELLED'
    STATUS_FINISHED = 'STATUS_FINISHED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_ACTIVE, 'Active'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_FINISHED, 'Finished'),
    ]

    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    specialist = models.ForeignKey(Specialist, on_delete=models.PROTECT)

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_PENDING)