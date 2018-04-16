from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Backscratcher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.FloatField()

    def __str__(self):
        return self.name


# generate a token whenever a new user is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
