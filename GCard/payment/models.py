# General Desc of Models -> https://github.com/lyk2017-django/GCard/wiki/Models#gcard-models-description

from django.db import models
from django.conf import settings
import uuid
import datetime

# Card Digit Generator -> https://github.com/lyk2017-django/GCard/wiki/Models#card_digit_gen-function

def card_digit_gen ():
    """
    This function provides us to generate 
    unique main card id
    """
    return uuid.uuid4().hex[:8]

# Card Model -> https://github.com/lyk2017-django/GCard/wiki/Models#card-model

class Card(models.Model):
     """
     This Model Provides Us To Generate Main Card
     """
     digits = models.CharField(max_length=8, default=card_digit_gen, unique=True)
     balance = models.PositiveSmallIntegerField(default=0)
     user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='card')
     def __str__(self):
        return "{no}".format(no=self.digits)
    
# Product Model -> https://github.com/lyk2017-django/GCard/wiki/Models#product-model

class Product(models.Model):
    """
    This Model Provides Us To Add 
    A Product To Database.
    """
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    brand = models.CharField(max_length=100, default="Unknown")
    image = models.URLField(default="http://lorempixel.com/240/240/technics/")
    def __str__(self):
        return "PK: {pk} \n Title: {title} \n Description: {desc} \n Price: {price} \n Image Url: {im}".format(title=self.title, desc=self.desc, price=self.price, im=self.image, pk=self.pk)

# Payment Card Digit Generator ->  https://github.com/lyk2017-django/GCard/wiki/Models#card_digit_gen-function-1
def paymentcard_digit_gen():
    """
    This function provides us to generate 
    unique disposable card id
    """
    return uuid.uuid4().hex[:10]

# Payment Card Model -> https://github.com/lyk2017-django/GCard/wiki/Models#card-model-1
class PaymentCard(models.Model):
    """
    This Model Provides Us To Generate 
    Disposable Card with Generated card ID (10 digits)
    """
    digits = models.CharField(max_length=10, default=paymentcard_digit_gen, unique=True)
    balance = models.PositiveSmallIntegerField(default=10)
    used = models.BooleanField(default=False)
    def __str__(self):
        return "Card No: {dig} \n Card Balance: {bal} \n Is Card Used: {used} ".format(dig=self.digits, bal=self.balance, used=self.used)

class Movement(models.Model):
    """
    This model provides us to keep
    transactions and show them to the
    user
    """
    movement_desc = models.CharField(max_length=100,blank=False,null=False)
    movement_type = models.BooleanField(null=False)
    movement_amount = models.SmallIntegerField(null=False)
    movement_card = models.ForeignKey(Card,on_delete=models.CASCADE)
    movement_date = models.DateTimeField(default=datetime.datetime.now)
    movement_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='movements', null=True)
    class Meta:
        get_latest_by = "m_date"
