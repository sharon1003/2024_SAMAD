# Generated by Django 3.0.3 on 2024-07-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='path',
            field=models.FilePathField(default='/Users/pengwenhsuan/Desktop/Deep-learning-model-deploy-with-django-master/media', path='/Users/pengwenhsuan/Desktop/Deep-learning-model-deploy-with-django-master/media'),
        ),
    ]
