# Generated by Django 4.1.7 on 2023-04-02 11:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkloop_app', '0004_alter_video_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_name',
            field=models.CharField(db_column='profile_name', default='', max_length=128, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator(message='Profile name can only contain letters, numbers, underscores, hyphens, and spaces.', regex='^[a-zA-Z0-9_\\- ]+$')]),
        ),
    ]