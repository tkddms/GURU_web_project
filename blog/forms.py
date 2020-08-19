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
            'title', 'head_image', 'missing_place', 'missing_date', 'missing_age','content', 'tags'
        ]
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'이름을 입력하세요.',
                }
            ),
            'head_image' : forms.FileInput(
                attrs={
                    'class' : 'form-control-file',
                }
            ),
            'missing_place': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'실종 장소를 입력하세요.'
                }
            ),
            'missing_date' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'datePicker',
                    'placeholder':'2020-01-01'
                }
            ),
            'missing_age' : forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'recent_age' : forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'그 외의 적고 싶은 내용들을 적으세요.',
                    'rows': 10,
                }
            ),
        }
        labels = {
            'title' : '이름',
            'head_image':'사진',
            'missing_place' : '실종 장소',
            'missing_date' : '실종 날짜',
            'missing_age' : '실종 당시 나이',
            'content' : '기타 정보',
        }