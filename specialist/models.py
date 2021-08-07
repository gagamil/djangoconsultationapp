from django.db import models
from django.contrib.auth.models import User


class Specialist(models.Model):
    '''
    - price: minimal units (cents). This approah is used by some gret web services (ex: Stripe)
    '''
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    price = models.IntegerField()