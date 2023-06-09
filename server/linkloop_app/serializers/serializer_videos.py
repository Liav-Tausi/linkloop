from django.db.models import Sum
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .serializer_profile import ProfileSerializer
from ..models import (
    Video,
    VideoLike,
    VideoComment,
    VideoImpression,
    ProfileImpression
)


class BaseVideoSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'

    def get_profile(self, obj):
        return ProfileSerializer(obj.user.profile).data


class CreateVideoSerializer(serializers.ModelSerializer):
    video_id_name = serializers.UUIDField()

    class Meta:
        model = Video
        fields = ('video_id_name', 'video_url', 'title', 'topic', 'description', 'user')

    def create(self, validated_data):
        print(validated_data)
        video = Video.objects.create(
            video_id_name=validated_data.get('video_id_name'),
            video_url=validated_data.get('video_url'),
            title=validated_data.get('title'),
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
    profile = serializers.SerializerMethodField()

    class Meta:
        model = VideoComment
        fields = '__all__'

    def get_profile(self, obj):
        return ProfileSerializer(obj.user.profile).data

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


class VideoImpressionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoImpression
        fields = '__all__'

    def create(self, validated_data):
        video_impression = VideoImpression.objects.create(
            viewer=validated_data.get('viewer'),
            video=validated_data.get('video')
        )
        return video_impression
