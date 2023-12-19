from django.dispatch import receiver
from django.db.models.signals import post_save
from home.models import Post
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_post(sender, instance, created, **kwargs):
    if created:
        content = f'Created Account as {instance.username}' 
        Post.objects.create(author=instance, content=content, is_deletable=False)
