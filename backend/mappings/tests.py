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

def test_get_doctors_for_patient(self):
    """Test retrieving all doctors assigned to Peter Parker"""
    # Assign Dr. Strange to Peter Parker
    mapping = PatientDoctorMapping.objects.create(patient=self.patient, doctor=self.doctor)
    response = self.client.get(f'/api/mappings/patient/{self.patient.id}/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['doctor'], self.doctor.id)

def test_duplicate_mapping(self):
    """Test assigning the same doctor to the same patient twice"""
    PatientDoctorMapping.objects.create(patient=self.patient, doctor=self.doctor)
    data = {
        'patient': self.patient.id,
        'doctor': self.doctor.id
    }
    response = self.client.post(self.mapping_url, data, format='json')
    self.assertEqual(response.status_code, 400)
    self.assertIn('This mapping already exists.', response.data['non_field_errors'])