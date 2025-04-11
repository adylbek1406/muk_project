from django.contrib import admin
from .models import *

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'phone_number', 'email')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('gender',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'experience', 'phone_number', 'email')
    search_fields = ('name', 'specialization', 'email')
    list_filter = ('specialization',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone_number', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('is_staff', 'is_active')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'date', 'time', 'status')
    search_fields = ('patient__username', 'doctor__name')
    list_filter = ('status', 'date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'rating', 'created_at')
    search_fields = ('patient__username', 'doctor__name')
    list_filter = ('rating', 'created_at')

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'status', 'created_at')
    search_fields = ('patient__username', 'doctor__name')
    list_filter = ('status', 'created_at')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'timestamp')
    search_fields = ('sender__username', 'receiver__username')
    list_filter = ('timestamp',)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'created_at')
    search_fields = ('patient__username', 'doctor__name')
    list_filter = ('created_at',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'amount', 'status', 'created_at')
    search_fields = ('patient__username', 'doctor__name')
    list_filter = ('status', 'created_at')
