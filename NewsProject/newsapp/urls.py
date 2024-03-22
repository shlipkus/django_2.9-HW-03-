from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(PostList.as_view()), name = 'post_list'),
    path('news/', cache_page(60*5)(NewsList.as_view()), name = 'news_list'),
    path('article/', cache_page(60*5)(ArticleList.as_view()), name = 'article_list'),
    path('<int:pk>', PostDetails.as_view(), name = 'post_detail'),
    path('news/<int:pk>', PostDetails.as_view(), name = 'post_detail'),
    path('article/<int:pk>', PostDetails.as_view(), name = 'post_detail'),
    path('news/create/', CreateNews.as_view(), name = 'news_create'),
    path('news/<int:pk>/update/', UpdateNews.as_view(), name = 'news_update'),
    path('news/<int:pk>/delete/', DeleteNews.as_view(), name = 'news_delete'),
    path('article/create/', CreateArticle.as_view(), name = 'article_create'),
    path('article/<int:pk>/update/', UpdateArticle.as_view(), name = 'article_update'),
    path('article/<int:pk>/delete/', DeleteArticle.as_view(), name = 'article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('create/', ChoiceCreate.as_view(), name='choice'),
]