from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from properties.models import Property


@receiver(post_save, sender=Property)
def property_post_save(sender, instance, created, **kwargs):
    """
    Signal handler that is called after a Property instance is saved.
    """
    cache.delete('all_properties')


@receiver(post_delete, sender=Property)
def property_post_delete(sender, instance, **kwargs):
    """
    Signal handler that is called after a Property instance is deleted.
    """
    cache.delete('all_properties')