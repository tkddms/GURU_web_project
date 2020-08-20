from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .forms import CommentForm, PostForm


def main(request):
    return render(request, 'blog/post_main.html')

def service(request):
    return render(request, 'blog/service.html')

def contact(request):
    return render(request, 'blog/contact.html')

class PostList(ListView):
    model = Post
    template_name = "post_list.html"
    def get_queryset(self):
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()

        return context

class PostCreate(CreateView):
    model = Post
    fields = [
        'title', 'head_image', 'missing_place', 'missing_date', 'missing_age', 'content',
    ]


def new_comment(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(comment.get_absolute_url())
    else:
        redirect('/blog/')

class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    
    def get_object(self, queryset=None):
        comment = super(CommentUpdate, self).get_object()
        if comment.author != self.request.user:
            raise PermissionError('댓글 수정 권한이 없습니다.')
        return comment


def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url() + '#comment-list')
    else:
        return redirect('/blog/')
