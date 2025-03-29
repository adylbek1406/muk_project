from django.db import models

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
