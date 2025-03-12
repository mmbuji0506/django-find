from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register_device/', views.register_device, name='register-device'),
    path('devices/', views.device_list, name='device-list'),
    path('devices/<int:device_id>/location/', views.device_location, name='device-location'),
    path('', views.home, name='home'),
]