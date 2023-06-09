# Generated by Django 4.1.7 on 2023-04-23 07:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkloop_app', '0021_education_education_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='education_name',
            field=models.CharField(db_column='education_name', max_length=128, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_level',
            field=models.PositiveSmallIntegerField(blank=True, db_column='rating', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(db_column='skill_name', max_length=128, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
