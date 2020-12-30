from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)
    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.URLField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media/slider/%Y')
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250, blank=True)
    facebook_link = models.URLField(max_length=250, blank=True)
    linkedIn_link = models.URLField(max_length=250, blank=True)
    youtube_link = models.URLField(
        max_length=250, blank=True, default='http://youtube.com')
    image = models.ImageField(upload_to='media/team/', blank=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    full_name = models.CharField(max_length=220)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    company = models.CharField(max_length=120)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name


class AboutModel(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image_url = models.URLField()
    description = RichTextField()

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = RichTextField()
