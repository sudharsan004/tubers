# Generated by Django 3.1.4 on 2020-12-28 16:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0010_auto_20201228_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]