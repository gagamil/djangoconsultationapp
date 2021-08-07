from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from client.models import Client
from specialist.models import Specialist
from order.models import Order


class OrderTests(APITestCase):
    def setUp(self):
        user_client = User.objects.create(username='clientuser', is_active=True)
        Client.objects.create(user=user_client)
        self.client.force_authenticate(user=user_client)

        user_specialist = User.objects.create(username='specialistuser', is_active=True)
        self.specialist = Specialist.objects.create(user=user_specialist, price=0)

    def test_create_order(self):
        url = reverse('new-order')
        data = {'specialist': self.specialist.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

        # specialit price is 0 so auto OK status (current implementation)
        self.assertEqual(Order.objects.get().status, Order.STATUS_OK)