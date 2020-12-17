from django.db import models

# Create your models here.


class Youtuber(models.Model):
    TEAM_CHOICES = (('solo', 'solo'), ('small team', 'small team'),
                    ['large team', 'large team'])
    name = models.CharField(max_length=200)
    categorey = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.IntegerField(verbose_name='heigth(cm)')
    camera = models.CharField(max_length=200, verbose_name='Camera Type')
    subscriber_count = models.IntegerField(verbose_name='Subscriber Count')
    price = models.IntegerField(verbose_name='Base Price')
    image = models.ImageField(upload_to='media/youtubers/%Y/%m')
    display_vedio_link = models.URLField(null=True)
    youtube_link = models.URLField(
        default='https://youtube.com', verbose_name='Youtube Channel Link')
    team = models.CharField(
        max_length=200, verbose_name='Team Type', choices=TEAM_CHOICES)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
