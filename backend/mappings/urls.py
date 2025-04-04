from django.urls import path
from .views import PatientDoctorMappingListCreateView, PatientDoctorMappingDetailView

urlpatterns = [
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list'),
    path('mappings/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
]
