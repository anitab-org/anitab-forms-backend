from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

ADM = 'admin'
STU = 'student'
USER = (
    (ADM, 'Admin'),
    (STU, 'Student'),
)

class UserInformation(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    user_type = models.CharField(
        max_length=7,
        choices=USER,
    )

    def __str__(self):

        return f'{self.name}: {self.user_type}'