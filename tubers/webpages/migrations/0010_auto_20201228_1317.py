# Generated by Django 3.1.4 on 2020-12-28 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0009_contactmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='phone',
            new_name='country',
        ),
    ]
