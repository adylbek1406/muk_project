from  rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'gender', 'address', 'phone_number', 'email']

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'experience', 'phone_number', 'image', 'email']

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name']


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number'),
            password=validated_data['password']
        )
        return user

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'time', 'status']

class RewiewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'patient', 'doctor', 'rating', 'comment', 'created_at']