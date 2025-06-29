from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a UserProfile for every new User"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Save the UserProfile whenever the User is saved"""
    # Check if the profile exists before saving
    try:
        instance.profile.save()
    except UserProfile.DoesNotExist:
        # Profile doesn't exist yet, it will be created by the create_profile signal
        pass