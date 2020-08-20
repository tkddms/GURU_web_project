from .models import Comment, Post
from django import forms
from markdownx.fields import MarkdownxFormField

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'head_image', 'missing_place', 'missing_date', 'missing_age','content',
        ]