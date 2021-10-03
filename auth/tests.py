from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse
from rest_framework.test import APITestCase


USERNAME = '123123'
EMAIL = '123123@example.com'
PASSWORD = 'qwertyuiop1234123'
User = get_user_model()


class SignInTestCase(APITestCase):
    def setUp(self) -> None:
        User.objects.create_user(USERNAME, EMAIL, PASSWORD)

    def test_signup(self):
        self.assertEqual(1, User.objects.count())
        url = reverse('login')
        data = {'email':EMAIL, 'password':PASSWORD}
        res = self.client.post(url, data, format='json')
        self.assertEqual(200, res.status_code)


class SignUpTestCase(APITestCase):
    def test_signup(self):
        # url = reverse('create')
        data = {'username':EMAIL, 'email':EMAIL, 'password':PASSWORD}
        res = self.client.post('/auth/users/', data, format='json')
        self.assertEqual(201, res.status_code)