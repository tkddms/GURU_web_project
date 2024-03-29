from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=300, blank=True)
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', default='/missing_img/missing_empty.jpg')

    SEX_CHOICES = (
        (1, "여성"),
        (2, "남성"),
    )
    sex = models.IntegerField(
        choices= SEX_CHOICES,
        default=1,
    )

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    missing_place = models.CharField(max_length=50)
    missing_date = models.DateField(max_length=20)
    missing_age = models.IntegerField(null=True)
    recent_age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)

    def get_update_url(self):
        return self.get_absolute_url() + 'update/'

    def get_markdown_content(self):
        return markdown(self.content)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_markdown_content(self):
        return markdown(self.text)

    def get_absolute_url(self):
        return self.post.get_absolute_url() + '#comment-id-{}'.format(self.pk)