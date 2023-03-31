from rest_framework import serializers

from articles.models import *


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title", "image","author", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"