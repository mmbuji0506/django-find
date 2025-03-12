from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from devices.models import Device
from .tasks import send_location_alert

class LocationCreate(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        device_id = self.request.query_params.get('device_id')
        try:
            device = Device.objects.get(id=device_id, user=self.request.user)
            instance = serializer.save(device=device)
            send_location_alert.delay(device.id, instance.latitude, instance.longitude) #Call the task.
        except Device.DoesNotExist:
            raise serializers.ValidationError("Device not found or not owned by user.")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LocationHistory(generics.ListAPIView):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        device_id = self.kwargs['device_id']
        try:
            device = Device.objects.get(id=device_id, user=self.request.user)
            return Location.objects.filter(device=device).order_by('-timestamp')
        except Device.DoesNotExist:
            return Location.objects.none() # Return an empty queryset if device not found.