from rest_framework import serializers

from preferences.models import MeetingPreference


class MeetingPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingPreference
        fields = ('when_min', 'when_max', 'where')
