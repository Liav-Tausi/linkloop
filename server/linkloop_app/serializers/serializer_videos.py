from django.db.models import Sum
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from moviepy.video.io.VideoFileClip import VideoFileClip

from linkloop_app.models import (
    Video,
    VideoLike,
    VideoComment,
    VideoImpression,
    ProfileImpression
)


class BaseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class CreateVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate(self, attrs):
        video_url = attrs.get('video_url')
        video = VideoFileClip(video_url)
        duration = video.duration
        if duration <= 30:
            raise ValidationError({"video": "Video must be less then 30 seconds."})
        return attrs

    def create(self, validated_data):
        video = Video.objects.create(
            video_url=validated_data.get('video_url'),
            topic=validated_data.get('topic'),
            description=validated_data.get('description'),
            user=validated_data.get('user')
        )
        return video


class LikeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLike
        fields = '__all__'

    def validate(self, attrs):
        try:
            video = Video.objects.get(id=attrs['video'].id)
        except Exception:
            raise ValidationError({"video": "No video found."})
        if video != attrs['video']:
            raise ValidationError({"video": "Invalid video."})
        return attrs

    def create(self, validated_data):
        like = VideoLike.objects.create(
            user=validated_data.get('user'),
            video=validated_data.get('video')
        )
        return like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoComment
        fields = '__all__'

    def validate(self, attrs):
        video_ids = Video.objects.all()
        if attrs.get('video') not in video_ids:
            raise ValidationError({"video": "No video found."})
        return attrs

    def create(self, validated_data):
        comment = VideoComment.objects.create(
            user=validated_data.get('user'),
            video=validated_data.get('video'),
            comment_text=validated_data.get('comment_text')
        )
        return comment


class ImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoImpression
        fields = '__all__'

    def validate(self, attrs):
        video_ids = Video.objects.all()
        if attrs.get('video') not in video_ids:
            raise ValidationError({"video": "No video found."})
        return attrs

    def create(self, validated_data):
        viewer = validated_data.get('viewer')
        if viewer is None:
            anonymous_views = \
                ProfileImpression.objects.filter(viewer=None).aggregate(Sum('anonymous_views'))[
                    'anonymous_views__sum'] or 0
            anonymous_views += 1
            impression = VideoImpression.objects.create(
                anonymous_views=anonymous_views,
                video=validated_data.get('video'),
            )
        else:
            impression = VideoImpression.objects.create(
                viewer=viewer,
                video=validated_data.get('video'),
            )
        return impression

