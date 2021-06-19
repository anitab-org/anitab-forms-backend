from django.db import models
from django.utils import timezone

from osp.models.user_information import UserInformation


class ZulipStat(models.Model):

    user_information = models.OneToOneField(UserInformation, on_delete=models.CASCADE)
    zulip_username = models.TextField(blank=True)
    total_messages = models.BigIntegerField(default=0)
    first_activity = models.DateTimeField(default=timezone.now)
    last_activity = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    newcomers_messages = models.BigIntegerField(default=0)
    general_messages = models.BigIntegerField(default=0)
    questions_messages = models.BigIntegerField(default=0)
    opportunities_messages = models.BigIntegerField(default=0)
    celebrate_messages = models.BigIntegerField(default=0)
