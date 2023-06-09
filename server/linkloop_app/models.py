from django.contrib.auth.models import User
from django.core.validators import (
    MinLengthValidator,
    MaxValueValidator,
    MinValueValidator
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Meta:
        db_table = "user_profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.URLField(verbose_name="profile_pic_url", blank=True, null=True)
    headline = models.CharField(db_column="headline", default="", blank=True, null=True, max_length=64,
                                validators=[MinLengthValidator(3)])
    about = models.TextField(db_column="about", blank=True, null=True, max_length=500,
                             validators=[MinLengthValidator(3)])
    location = models.CharField(db_column="location", default="", blank=True, null=True, max_length=128,
                                validators=[MinLengthValidator(10)])
    rating = models.PositiveSmallIntegerField(db_column="rating", blank=True, null=True,
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_time = models.DateTimeField(db_column="created_time", auto_now_add=True)
    updated_time = models.DateTimeField(db_column="updated_time", auto_now=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Video(models.Model):
    class Meta:
        db_table = "video"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    video_id_name = models.CharField(max_length=36, unique=True, editable=False, default='')
    video_url = models.URLField(verbose_name="video_url", blank=False, null=False, max_length=128)
    topic = models.CharField(db_column="topic", blank=False, null=False, max_length=64,
                             validators=[MinLengthValidator(1)])
    title = models.CharField(db_column="title", blank=False, null=False, max_length=64,
                             validators=[MinLengthValidator(1)])
    description = models.TextField(db_column="description", blank=False, null=False, max_length=150,
                                   validators=[MinLengthValidator(1)])
    created_time = models.DateTimeField(db_column="created_time", auto_now_add=True)
    updated_time = models.DateTimeField(db_column="updated_time", auto_now=True)


class VideoLike(models.Model):
    class Meta:
        db_table = "video_like"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    created_time = models.DateTimeField(db_column="created_time", auto_now_add=True)
    updated_time = models.DateTimeField(db_column="updated_time", auto_now=True)


class VideoComment(models.Model):
    class Meta:
        db_table = "video_comment"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment_text = models.TextField(db_column="comment_text", blank=False, null=False, max_length=500,
                                    validators=[MinLengthValidator(1)])
    created_time = models.DateTimeField(db_column="created_time", auto_now_add=True)
    updated_time = models.DateTimeField(db_column="updated_time", auto_now=True)


class VideoImpression(models.Model):
    class Meta:
        db_table = "video_impression"

    viewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    impression_duration = models.TimeField(db_column="impression_duration", blank=True, null=True)
    impression_time = models.DateTimeField(db_column="impression_time", auto_now_add=True)


class Skill(models.Model):
    class Meta:
        db_table = "skill"

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    skill_name = models.CharField(db_column="skill_name", max_length=128, blank=False, null=False,
                                  validators=[MinLengthValidator(3)], unique=True)
    skill_level = models.PositiveSmallIntegerField(db_column="rating", blank=True, null=True,
                                                   validators=[MinValueValidator(1), MaxValueValidator(6)])
    created_time = models.DateTimeField(db_column="created_time", auto_now_add=True)
    updated_time = models.DateTimeField(db_column="updated_time", auto_now=True)


class Education(models.Model):
    class Meta:
        db_table = "education"

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    education_name = models.CharField(db_column="education_name", blank=False, null=False, max_length=128,
                                      validators=[MinLengthValidator(5)], unique=True)
    school_name = models.CharField(db_column="school_name", blank=False, null=False, max_length=128,
                                   validators=[MinLengthValidator(5)])
    education_description = models.TextField(db_column="education_description", blank=False, null=False, max_length=300,
                                             validators=[MinLengthValidator(1)], default="")
    start_date = models.DateField(db_column="start_date", blank=False, null=False)
    end_date = models.DateField(db_column="end_date", blank=True, null=True)
    created_time = models.DateTimeField(db_column="created_time", auto_now_add=True)
    updated_time = models.DateTimeField(db_column="updated_time", auto_now=True)


class Experience(models.Model):
    class Meta:
        db_table = "experience"

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    experience_name = models.CharField(db_column="experience_name", blank=False, null=False, max_length=128,
                                       validators=[MinLengthValidator(1)], unique=True)
    experience_description = models.TextField(db_column="experience_description", blank=False, null=False,
                                              max_length=300, validators=[MinLengthValidator(1)], unique=True)
    start_date = models.DateField(db_column="start_date", blank=False, null=False)
    end_date = models.DateField(db_column="end_date", blank=True, null=True)
    created_time = models.DateTimeField(db_column="created_time", auto_now_add=True)
    updated_time = models.DateTimeField(db_column="updated_time", auto_now=True)


class ProfileImpression(models.Model):
    class Meta:
        db_table = "profile_impression"

    viewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viewed_impressions', null=True, blank=True)
    viewed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='impressions')
    viewed_time = models.DateTimeField(db_column="viewed_time", auto_now_add=True)


class UserSearch(models.Model):
    class Meta:
        db_table = "user_search"

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    search_query = models.CharField(db_column="search_query", blank=False, null=False, max_length=300,
                                    validators=[MinLengthValidator(1)])
    search_time = models.DateTimeField(db_column="search_time", auto_now_add=True)


class Message(models.Model):
    class Meta:
        db_table = "message"

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_message', default='')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_message', default='')
    title = models.CharField(db_column="title", blank=False, null=False, max_length=128,
                             validators=[MinLengthValidator(5)])
    description = models.TextField(db_column="description", blank=False, null=False, max_length=300,
                                   validators=[MinLengthValidator(1)])
    message_text = models.TextField(db_column="message_text", blank=False, null=False, max_length=1000,
                                    validators=[MinLengthValidator(10)], default='')
    location = models.CharField(db_column="location", blank=False, null=False, max_length=128,
                                validators=[MinLengthValidator(5)])
    created_time = models.DateTimeField(db_column="created_time", auto_now_add=True)
    updated_time = models.DateTimeField(db_column="updated_time", auto_now=True)
