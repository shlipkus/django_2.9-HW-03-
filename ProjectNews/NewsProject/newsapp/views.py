from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .filters import NewsFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        qs = queryset.filter(postType = 'NW')
        return qs


class ArticleList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'articles.html'
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        qs = queryset.filter(postType = 'AR')
        return qs

class PostDetails(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class CreateNews(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postType = 'NW'
        return super().form_valid(form)


class CreateArticle(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postType = 'AR'
        return super().form_valid(form)


class UpdateNews(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postType = 'NW'
        return super().form_valid(form)


class UpdateArticle(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postType = 'AR'
        return super().form_valid(form)


class DeleteNews(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')


class DeleteArticle(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')