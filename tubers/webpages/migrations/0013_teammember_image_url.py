# Generated by Django 3.1.4 on 2020-12-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0012_aboutmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='image_url',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]
