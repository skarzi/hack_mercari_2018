from django.db import models


class MeetingPreference(models.Model):
    when = models.DateTimeField()
    where = models.TextField()
