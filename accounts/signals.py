from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_verification_email(sender, instance, created, **kwargs):
    """Send verification email when a new user is created."""
    if created and not instance.is_email_verified:
        # TODO: Implement email verification logic
        pass
