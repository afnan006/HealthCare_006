from django.urls import path
from .views import PatientDoctorMappingListCreateView, PatientDoctorMappingDetailView, PatientDoctorMappingByPatientView

urlpatterns = [
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list'),
    path('mappings/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
    path('mappings/patient/<int:patient_id>/', PatientDoctorMappingByPatientView.as_view(), name='mapping-by-patient'),

]
