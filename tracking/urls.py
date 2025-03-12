from django.urls import path
from .views import LocationCreate, LocationHistory

urlpatterns = [
    path('update/', LocationCreate.as_view(), name='location-update'),
    path('history/<int:device_id>/', LocationHistory.as_view(), name='location-history'),
]