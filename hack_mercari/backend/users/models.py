from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    eth_address = models.CharField(max_length=42)
    is_courier = models.BooleanField(default=False)
