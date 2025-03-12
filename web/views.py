from django.shortcuts import render, redirect, get_object_or_404
from devices.models import Device
from tracking.models import Location
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import DeviceRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('device-list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('device-list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def register_device(request):
    form = DeviceRegistrationForm()
    return render(request, 'device_registration_form.html', {'form': form})

@login_required
def device_list(request):
    devices = Device.objects.filter(user=request.user)
    if request.method == 'POST':
        form = DeviceRegistrationForm(request.POST)
        print("POST data received:", request.POST)  # CRUCIAL
        if form.is_valid():
            print("Form is valid")
            device = form.save(commit=False)
            device.user = request.user
            device.save()
            print("Device saved")  # Add this
            return redirect('device-list')
        else:
            print("Form is invalid")
            print(form.errors)
    else:
        form = DeviceRegistrationForm()
    return render(request, 'device_list.html', {'form': form, 'devices': devices})

@login_required
def device_location(request, device_id):
    try:
        device = get_object_or_404(Device, id=device_id, user=request.user)
        print("Device:", device)
    except Exception as e:
        print("Error retrieving device:", e)
        return HttpResponse("Error retrieving device", status=500)

    try:
        locations = Location.objects.filter(device=device).order_by('-timestamp')
        print("Locations:", locations)
        print("Locations QuerySet:", locations.query)
    except Exception as e:
        print("Error retrieving locations:", e)
        return HttpResponse("Error retrieving locations", status=500)

    return render(request, 'device_location.html', {'device': device, 'locations': locations})

def home(request):
    return render(request, 'home.html')