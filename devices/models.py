from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Device(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100, blank=True, null=True)  # Add this
    model_name = models.CharField(max_length=100, blank=True, null=True)  # Add this
    serial_number = models.CharField(max_length=100, blank=True, null=True)  # Add this
    imei = models.CharField(max_length=100, blank=True, null=True)        # Add this
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name