from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from osp.utils import user_types

class UserInformation(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    user_type = models.CharField(
        max_length=7,
        choices=user_types.USERS,
        default='student'
    )

    def __str__(self):
        return f'{self.name}: {self.user_type}'
