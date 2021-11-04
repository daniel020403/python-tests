from rest_framework import serializers
from datetime import datetime
import base64

class GeoLocationSerializer(serializers.Serializer):
    coordinates = serializers.CharField()

    def get_info(self, coord):
        decoded     = base64.b64decode(coord).decode()
        exploded    = decoded.split('|')

        geo_dict                = {}
        geo_dict['user_id']     = int(exploded[0])
        geo_dict['timestamp']   = datetime.fromtimestamp(int(exploded[1])).strftime('%Y-%m-%d %H:%M:%S')
        geo_dict['longitude']   = float(exploded[2])
        geo_dict['latitude']    = float(exploded[3])

        return geo_dict

class Webhook:
    def __init__(self, coordinates):
        self.coordinates = coordinates
