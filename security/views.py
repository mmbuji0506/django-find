from rest_framework import generics, permissions, serializers
from devices.models import Device
from rest_framework.response import Response
from rest_framework import status

class RemoteLock(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, device_id):
        try:
            device = Device.objects.get(id=device_id, user=request.user)
            # In a real app, you would send a command to the device to lock itself.
            # This is a placeholder for that functionality.
            # For demonstration, we'll just update the device's last_seen timestamp.
            device.save()
            return Response({"message": f"Remote lock command sent to device {device.name}."}, status=status.HTTP_200_OK)
        except Device.DoesNotExist:
            return Response({"error": "Device not found or not owned by user."}, status=status.HTTP_404_NOT_FOUND)
        
class RemoteWipe(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, device_id):
        try:
            device = Device.objects.get(id=device_id, user=request.user)
            # In a real app, you would send a command to the device to wipe itself.
            # This is a placeholder for that functionality.
            # For demonstration, we'll just update the device's last_seen timestamp.
            device.save()
            return Response({"message": f"Remote wipe command sent to device {device.name}."}, status=status.HTTP_200_OK)
        except Device.DoesNotExist:
            return Response({"error": "Device not found or not owned by user."}, status=status.HTTP_404_NOT_FOUND)