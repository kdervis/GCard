from django.db import models
from django.conf import settings
import uuid

class Card(models.Model):
     digits = models.CharField(max_length=8, default=uuid.uuid4().hex[:8])
     balance = models.PositiveSmallIntegerField()


class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveSmallIntegerField()
    image = models.URLField()

class PaymentCard(models.Model):
    digits = models.CharField(max_length=10, default=uuid.uuid4().hex[:10])
    balance = models.PositiveSmallIntegerField()
    used = models.BooleanField()

