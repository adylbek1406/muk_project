from django.urls import path

from . import views

urlpatterns = [
    path('patients/', views.PatientViewSet.as_view({'get': 'list'})),
    path('patients/<int:pk>/', views.PatientViewSet.as_view({'get': 'retrieve'})),
    path('doctors/', views.DoctorViewSet.as_view({'get': 'list'})),
    path('doctors/<int:pk>/', views.DoctorViewSet.as_view({'get': 'retrieve'})),
]