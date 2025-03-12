from django.urls import path
from .views import RemoteLock, RemoteWipe

urlpatterns = [
    path('lock/<int:device_id>/', RemoteLock.as_view(), name='remote-lock'),
    path('wipe/<int:device_id>/', RemoteWipe.as_view(), name='remote-wipe'),
]