from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

POSITION = [
    ('AR','Article'),
    ('NW','News')
]


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        post_rate = self.post_set.aggregate(a = Sum('rating'))['a'] #так как метод возвращает словарь решил взять значение таким способом
        if post_rate == None:
            post_rate = 0                #если у автора нет постов метод возвращает None и возникает ошибка. Добовляем костыль.
        comm_rate = self.authorUser.comment_set.aggregate(b = Sum('rating'))['b']
        if comm_rate == None:
            comm_rate = 0

        self.rating_author = post_rate*3 + comm_rate
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.category}'


class Post(models.Model):
    article = 'AR'
    news = 'NW'

    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    postType = models.CharField(max_length=2, choices=POSITION, default=article)
    time_in = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField(default='Контент')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:123]+'...'

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.category}'


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
