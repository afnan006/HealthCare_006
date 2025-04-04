from django.test import TestCase
from rest_framework.test import APIClient
from authentication.models import User
from patients.models import Patient

class PatientTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='tony_stark', email='tony@starkindustries.com', password='ironman123')
        self.client.force_authenticate(user=self.user)
        self.patient_url = '/api/patients/'

    def test_create_patient(self):
        """Test creating a patient (Peter Parker)"""
        data = {
            'name': 'Peter Parker',
            'age': 18,
            'gender': 'Male',
            'address': 'Queens, New York'
        }
        response = self.client.post(self.patient_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.first().created_by, self.user)

    def test_retrieve_patients(self):
        """Test retrieving all patients created by Tony Stark"""
        Patient.objects.create(name='Deadpool', age=30, gender='Male', address='Unknown', created_by=self.user)
        response = self.client.get(self.patient_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)