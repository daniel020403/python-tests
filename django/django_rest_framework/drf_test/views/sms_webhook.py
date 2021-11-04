from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_test.serializers import GeoLocationSerializer
from drf_test.models import Geolocation

class SmsWebhookViewSet(viewsets.ViewSet):

    def create(self, request):

        serializer  = GeoLocationSerializer(request.data)
        info        = serializer.get_info(serializer.data['coordinates'])
        geolocation = Geolocation(
            user_id     = info['user_id'],
            timestamp   = info['timestamp'],
            longitude   = info['longitude'],
            latitude    = info['latitude']
        )
        geolocation.save()

        return Response('', status=status.HTTP_200_OK)
