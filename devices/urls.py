from django.urls import path
from .views import DeviceCreate

urlpatterns = [
    path('register/', DeviceCreate.as_view(), name='device-register'),
]