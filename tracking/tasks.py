# tracking/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from devices.models import Device

@shared_task
def send_location_alert(device_id, latitude, longitude):
    try:
        device = Device.objects.get(id=device_id)
        subject = f"Location Alert: {device.name}"
        message = f"Your device {device.name} has reported a new location: Latitude: {latitude}, Longitude: {longitude}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [device.user.email])
    except Device.DoesNotExist:
        print(f"Device with ID {device_id} not found.")