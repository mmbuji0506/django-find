from django.db import models
from devices.models import Device

class Location(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    accuracy = models.FloatField(blank=True, null=True) #in meters

    def __str__(self):
        return f"Location of {self.device.name} at {self.timestamp}"