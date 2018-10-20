from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from deliveries.models import Delivery
from preferences.models import MeetingPreference
from preferences.serializers import MeetingPreferenceSerializer
from users.models import User


class DeliverySerializer(serializers.ModelSerializer):
    sender = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    recipient = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    courier = SlugRelatedField(
        slug_field='username',
        read_only=True,
        allow_null=True
    )

    class Meta:
        model = Delivery
        fields = (
            'id', 'description', 'sender', 'recipient', 'courier',
            'status', 'sender_preference', 'recipient_preference'
        )
        depth = 2


class CreateDeliverySerializer(serializers.ModelSerializer):
    recipient = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.filter(is_courier=False)
    )
    sender_preference = MeetingPreferenceSerializer()

    class Meta:
        model = Delivery
        fields = (
            'description', 'recipient', 'sender_preference'
        )

    def create(self, validated_data):
        sender_preference_data = validated_data.pop("sender_preference")
        delivery = super().create(validated_data)
        delivery.sender_preference = MeetingPreference.objects.create(
            **sender_preference_data
        )
        delivery.save(update_fields=["sender_preference"])
        return delivery
