# Generated by Django 3.1.4 on 2020-12-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]