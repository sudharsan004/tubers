from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class ContactInfo(models.Model):
    email = models.EmailField()
    phone = PhoneNumberField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    youtube_link = models.URLField()

    def __str__(self):
        return 'Hiretuber Contact Info'
