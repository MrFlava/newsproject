from rest_framework import serializers
from django.shortcuts import get_object_or_404

from news.models import Post, Comment, Upvote


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class UpvoteSerializer(serializers.ModelSerializer):
    voted = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = Upvote
        fields = "__all__"

    def create(self, validated_data):
        upvote_obj = super().create(validated_data)
        post = validated_data.pop("post")
        post = get_object_or_404(Post, pk=post.pk)
        post.upvotes_amount += 1
        post.save()
        return upvote_obj
