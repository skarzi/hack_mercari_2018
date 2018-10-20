from django.db import models

from services.pusher import PusherClient


class Delivery(models.Model):
    STATUS_ASSIGNING = 'assigning'
    STATUS_WAITING_FOR_COURIER = 'waiting_for_courier'
    STATUS_IN_TRANSIT = 'in_transit'
    STATUS_DELIVERED = 'delivered'
    STATUS_CHOICES = (
        (STATUS_ASSIGNING, 'Assigning to courier'),
        (STATUS_WAITING_FOR_COURIER, 'Waiting for courier to pick up'),
        (STATUS_IN_TRANSIT, 'Package is on it\'s way'),
        (STATUS_DELIVERED, 'Package delivered')
    )
    description = models.TextField()
    sender = models.ForeignKey(
        'users.User',
        related_name='+',
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        'users.User',
        related_name='+',
        on_delete=models.CASCADE
    )
    courier = models.ForeignKey(
        'users.User',
        related_name='+',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default=STATUS_ASSIGNING
    )
    sender_preference = models.OneToOneField(
        'preferences.MeetingPreference',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True, blank=True
    )
    recipient_preference = models.OneToOneField(
        'preferences.MeetingPreference',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True, blank=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.push_notifications()

    def push_notifications(self):
        push_recipients = [
            self.sender.username, self.recipient.username
        ]
        if self.courier:
            push_recipients.append(self.courier.username)
        PusherClient.trigger(
            push_recipients, 'delivery-updated', {}
        )
