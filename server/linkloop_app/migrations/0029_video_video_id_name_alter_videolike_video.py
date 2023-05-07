# Generated by Django 4.1.7 on 2023-04-30 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkloop_app', '0028_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_id_name',
            field=models.CharField(default='', editable=False, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='videolike',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='linkloop_app.video'),
        ),
    ]