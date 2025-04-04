from django.test import TestCase
from rest_framework.test import APIClient
from authentication.models import User
from patients.models import Patient
from doctors.models import Doctor
from mappings.models import PatientDoctorMapping

class MappingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='tony_stark', email='tony@starkindustries.com', password='ironman123')
        self.client.force_authenticate(user=self.user)
        self.patient = Patient.objects.create(name='Peter Parker', age=18, gender='Male', address='Queens', created_by=self.user)
        self.doctor = Doctor.objects.create(name='Dr. Strange', specialization='Neurosurgeon', phone='+1234567890', email='strange@sorcerer.com')
        self.mapping_url = '/api/mappings/'

    def test_assign_doctor_to_patient(self):
        """Test assigning Dr. Strange to Peter Parker"""
        data = {
            'patient': self.patient.id,
            'doctor': self.doctor.id
        }
        response = self.client.post(self.mapping_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(PatientDoctorMapping.objects.count(), 1)