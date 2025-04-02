from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)  # Позволяет пустые значения
    email = models.EmailField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username

class Appointment(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')],
        default='pending'
    )

    def __str__(self):
        return f"{self.patient} -> {self.doctor} ({self.date} {self.time})"

class Review(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Оценка от 1 до 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} -> {self.doctor} ({self.rating})"
