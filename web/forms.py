from django import forms
from devices.models import Device

class DeviceRegistrationForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'product_name', 'model_name', 'serial_number', 'imei']