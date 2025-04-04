from django.test import TestCase
from rest_framework.test import APIClient
from authentication.models import User
from doctors.models import Doctor

class DoctorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='tony_stark', email='tony@starkindustries.com', password='ironman123')
        self.client.force_authenticate(user=self.user)
        self.doctor_url = '/api/doctors/'

    def test_create_doctor(self):
        """Test creating a doctor (Dr. Strange)"""
        data = {
            'name': 'Dr. Strange',
            'specialization': 'Neurosurgeon',
            'phone': '+1234567890',
            'email': 'strange@sorcerer.com'
        }
        response = self.client.post(self.doctor_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Doctor.objects.count(), 1)

    def test_retrieve_doctors(self):
        """Test retrieving all doctors"""
        Doctor.objects.create(name='Wanda Maximoff', specialization='Psychiatrist', phone='+9876543210', email='wanda@avengers.com')
        response = self.client.get(self.doctor_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)