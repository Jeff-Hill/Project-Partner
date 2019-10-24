from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Owner(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True, max_length=300, height_field='url_height', width_field='url_width')


@receiver(post_save, sender=User)
def create_owner(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_owner(sender, instance, **kwargs):
    instance.owner.save()

