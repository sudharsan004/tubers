from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from youtubers.models import Ytuber
# Create your models here.


class ContactInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=400)
    user_id = models.IntegerField(null=True, blank=True)
    ytuber_contacted = models.ForeignKey(Ytuber, on_delete=models.CASCADE)
    date_contacted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
