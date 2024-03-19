from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from .tasks import post_create_notify
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def categories_changed(sender, instance, action, *args, **kwargs):
    if action == 'post_add':
        post_id = instance.pk
        post_create_notify.delay(post_id)
