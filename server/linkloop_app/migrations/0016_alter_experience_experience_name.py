# Generated by Django 4.1.7 on 2023-04-17 11:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkloop_app', '0015_alter_profile_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='experience_name',
            field=models.CharField(db_column='experience_name', max_length=128, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
