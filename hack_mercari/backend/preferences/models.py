from django.db import models


class MeetingPreference(models.Model):
    when_min = models.DateTimeField()
    when_max = models.DateTimeField()

    where = models.TextField()
