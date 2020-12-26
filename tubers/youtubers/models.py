from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from urllib.parse import urlparse, parse_qs
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Ytuber(models.Model):
    TEAM_CHOICES = (
        ('solo', 'solo'),
        ('small ', 'small '),
        ('large ', 'large ')
    )
    CAMERA_CHOICES = (
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('panasonic', 'panasonic'),
        ('others', 'others')
    )
    CATEGOREY_CHOICES = (
        ('cooking', 'cooking'),
        ('lifestyle', 'lifestyle'),
        ('comedy', 'comedy'),
        ('tech', 'tech'),
        ('music', 'music'),
        ('kids', 'kids'),
        ('gaming', 'gaming'),
        ('travel', 'travel'),
        ('others', 'others')
    )

    name = models.CharField(max_length=200)
    email = models.EmailField(default='8921test@gmail.com')
    city = models.CharField(max_length=200)
    age = models.IntegerField()
    youtube_channel_name = models.CharField(max_length=150)
    youtube_channel_link = models.URLField(default='https://youtube.com')
    subscriber_count = models.IntegerField(verbose_name='Subscriber Count')
    camera_type = models.CharField(max_length=200, choices=CAMERA_CHOICES)
    categorey = models.CharField(max_length=200, choices=CATEGOREY_CHOICES)
    team_type = models.CharField(max_length=200, choices=TEAM_CHOICES)
    price = models.IntegerField(verbose_name='Base Price')
    image = models.ImageField(
        upload_to='media/youtubers/%Y/%m', verbose_name='dp image (dp image or dp Url)', blank=True)
    image_url = models.URLField(
        verbose_name='Dp URL', blank=True)
    display_vedio_link = models.URLField(null=True)

    def video_id(self):
        query = urlparse(self.display_vedio_link)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse_qs(query.query)
                return p['v'][0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
    description = RichTextField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactTuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.PhoneNumberField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=400)
    contacted_ytuber = models.ForeignKey(Ytuber, on_delete=models.CASCADE)
