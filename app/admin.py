from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Review)
admin.site.register(ConsultationRequest)
admin.site.register(Message)
admin.site.register(Prescription)
admin.site.register(Payment)
