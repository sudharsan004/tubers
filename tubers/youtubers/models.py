from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
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
    description = RichTextField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        super(Ytuber, self).clean()
        if self.image is None and self.image_url is None:
            raise ValidationError('Validation error text')
