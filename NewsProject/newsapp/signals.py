from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def categories_changed(sender, instance, action, *args, **kwargs):
        if action == 'post_add':
                cat = instance.categories.all()
                emails = User.objects.filter(
                         subscriptions__category=cat[0]
                 ).values_list('email', flat=True)

                subject = f'Новая публикация в категории {cat[0]}'

                text_content = (
                        f'Пост: {instance.title}\n'
                        f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
                )

                html_content = (
                        f'Пост: {instance.title}<br>'
                        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
                        f'Ссылка на пост</a>'
                )
                for email in emails:
                        msg = EmailMultiAlternatives(subject, text_content, None, [email])
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()





