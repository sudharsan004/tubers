# Generated by Django 3.1.4 on 2020-12-16 11:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teammember',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='teammember',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/team/'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='linkedIn_link',
            field=models.URLField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='teammember',
            name='role',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
