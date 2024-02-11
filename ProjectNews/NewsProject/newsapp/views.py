from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'


class PostDetails(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'