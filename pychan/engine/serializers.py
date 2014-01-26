from django.contrib.auth.models import User
from engine.models import Post, Reply
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('post_id', 'author_name', 'author_email', 'post_subject', 'post_body', 'image')


class ReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reply
        fields = ('reply_id', 'op_post_id', 'reply_name', 'reply_email', 'reply_body', 'image')
