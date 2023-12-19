from django.dispatch import receiver
from django.db.models.signals import post_save
from authentication.models import UserProfile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(instance,sender, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, contact_number='9800000000')

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()