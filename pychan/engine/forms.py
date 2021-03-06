from django.forms import ModelForm
from engine.models import Post, Reply


class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ('post_subject', 'post_body', 'image')


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body', 'image')
