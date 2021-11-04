from django.db import models

class Geolocation(models.Model):
    user_id     = models.IntegerField(null=True)
    timestamp   = models.DateTimeField()
    longitude   = models.FloatField()
    latitude    = models.FloatField()
