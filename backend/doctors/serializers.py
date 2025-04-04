from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_phone(self, value):
        if not value.startswith('+'):
            raise serializers.ValidationError("Phone number must start with '+'.")
        return value