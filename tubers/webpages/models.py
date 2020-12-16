from django.db import models

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)
    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.URLField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media/slider/%Y')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250, blank=True)
    facebook_link = models.URLField(max_length=250, blank=True)
    linkedIn_link = models.URLField(max_length=250, blank=True)
    image = models.ImageField(upload_to='media/team/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
