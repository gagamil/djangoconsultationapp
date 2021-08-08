from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from client.models import Client
from specialist.models import Specialist
from consultation.models import Consultation


class ConsultationTests(APITestCase):
    def setUp(self):
        user_client = User.objects.create(username='clientuser', is_active=True)
        self.app_client = Client.objects.create(user=user_client)
        self.client.force_authenticate(user=user_client)

        self.user_specialist = User.objects.create(username='specialistuser', is_active=True)
        self.app_specialist = Specialist.objects.create(user=self.user_specialist, price=0)

    def test_start_consultation(self):
        fake_id = 12345
        # no consultation with provided id exists
        url = reverse('update-consultation', kwargs={'pk':fake_id})
        data = {'status': Consultation.STATUS_ACTIVE}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # create consultation and let one of the users start (set status)
        consultation = Consultation.objects.create(client=self.app_client, specialist=self.app_specialist)
        url = reverse('update-consultation', kwargs={'pk':consultation.id})
        data = {'status': Consultation.STATUS_ACTIVE}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Consultation.objects.filter(status=Consultation.STATUS_ACTIVE).count(), 1)

        # end consultation (set status)
        data = {'status': Consultation.STATUS_FINISHED}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Consultation.objects.filter(status=Consultation.STATUS_FINISHED).count(), 1)

    def test_rtc_connection_token_generation_view_200(self):
        '''
        Test both specialist and client may fetch the access token to establish rtc connection.
        '''
        consultation = Consultation.objects.create(client=self.app_client, specialist=self.app_specialist)
        url = reverse('get-rtc-token', kwargs={'pk':consultation.id})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.force_authenticate(user=self.user_specialist)
        url = reverse('get-rtc-token', kwargs={'pk':consultation.id})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rtc_connection_token_generation_view_404(self):
        consultation = Consultation.objects.create(client=self.app_client, specialist=self.app_specialist)

        user_client = User.objects.create(username='clientuser2', is_active=True)
        app_client = Client.objects.create(user=user_client)
        self.client.force_authenticate(user=user_client)

        url = reverse('get-rtc-token', kwargs={'pk':consultation.id})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ConsultationTests(APITestCase):
    def test_callback(self):
        url = reverse('twilio-room-status-update')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)