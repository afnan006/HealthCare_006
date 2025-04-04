from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/auth/register/'
        self.login_url = '/api/auth/login/'

    def test_register_user(self):
        """Test registering a new user (Tony Stark)"""
        data = {
            'username': 'tony_stark',
            'email': 'tony@starkindustries.com',
            'password': 'ironman123'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)

    def test_login_user(self):
        """Test logging in an existing user (Tony Stark)"""
        User.objects.create_user(username='tony_stark', email='tony@starkindustries.com', password='ironman123')
        data = {
            'email': 'tony@starkindustries.com',
            'password': 'ironman123'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)