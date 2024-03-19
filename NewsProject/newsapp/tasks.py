from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

from .management.commands.runapscheduler import my_job
from .models import Post


@shared_task
def post_create_notify(post_id):
    post = Post.objects.get(pk=post_id)
    cat = post.categories.all()
    emails = User.objects.filter(
        subscriptions__category=cat[0]
    ).values_list('email', flat=True)

    subject = f'Новая публикация в категории {cat[0]}'

    text_content = (
        f'Пост: {post.title}\n'
        f'Ссылка на пост: http://127.0.0.1:8000{post.get_absolute_url}'
    )

    html_content = (
        f'Пост: {post.title}<br>'
        f'<a href="http://127.0.0.1:8000{post.get_absolute_url}">'
        f'Ссылка на пост</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task
def week_newsletter():
    my_job()