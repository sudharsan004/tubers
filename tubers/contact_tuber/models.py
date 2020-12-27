from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from youtubers.models import Ytuber
# Create your models here.


class ContactInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = PhoneNumberField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=400)
    ytuber_contacted = models.ForeignKey(Ytuber, on_delete=models.CASCADE)
    date_contacted = models.DateTimeField(auto_now_add=True)
