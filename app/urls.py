from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PatientViewSet, DoctorViewSet, RegisterView, AppointmentViewSet, ReviewViewSet

# Создаем роутер
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename="patient")
router.register(r'doctors', DoctorViewSet, basename="doctor")
router.register(r'appointments', AppointmentViewSet, basename="appointment")
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    # Подключаем роутер к `urlpatterns`
    path('', include(router.urls)),

    # Регистрация (создание пользователя)
    path('register/', RegisterView.as_view(), name='register'),

    # Аутентификация (получение токена)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Обновление токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
