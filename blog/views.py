from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title', 'head_image', 'content'
    ]

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title', 'head_image', 'content'
    ]

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(type(self),self).form_valid(form)
        else:
            return redirect('/blog/')