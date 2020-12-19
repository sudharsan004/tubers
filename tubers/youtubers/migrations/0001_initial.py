# Generated by Django 3.1.4 on 2020-12-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('categorey', models.CharField(choices=[('cooking', 'cooking'), ('comedy', 'comedy'), ('tech', 'tech'), ('music', 'music'), ('kids', 'kids'), ('gaming', 'gaming'), ('travel', 'travel'), ('others', 'others')], max_length=200)),
                ('display_vedio_link', models.URLField(null=True)),
                ('description', models.CharField(max_length=350)),
                ('city', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField(verbose_name='heigth(cm)')),
                ('camera_type', models.CharField(choices=[('canon', 'canon'), ('nikon', 'nikon'), ('sony', 'sony'), ('panasonic', 'panasonic'), ('others', 'others')], max_length=200)),
                ('subscriber_count', models.IntegerField(verbose_name='Subscriber Count')),
                ('price', models.IntegerField(verbose_name='Base Price')),
                ('image', models.ImageField(upload_to='media/youtubers/%Y/%m')),
                ('youtube_channel_link', models.URLField(default='https://youtube.com')),
                ('team_type', models.CharField(choices=[('solo', 'solo'), ('small team', 'small team'), ('large team', 'large team')], max_length=200)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
