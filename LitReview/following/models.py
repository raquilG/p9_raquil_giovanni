from django.db import models
from django.conf import settings


# Create your models here.
class UserFollows(models.Model):
    class Meta:
        unique_together = ('user', 'followed_user', )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following')

    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by')

    # Your UserFollows model definition goes here
