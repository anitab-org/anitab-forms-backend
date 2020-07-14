from django.db import models

from osp.models.question import Question
from osp.models.abstract_timestamp import AbstractTimestamp
from osp.utils import target_user_types, status_types

class Form(AbstractTimestamp):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published_status = models.CharField(
        max_length=11,
        choices=status_types.STATUS_TYPES,
        default='unpublished'
    )
    questions = models.ManyToManyField(
        to=Question,
        default=None,
        blank=True,
        related_name='forms'
    )
    target_user = models.CharField(
        max_length=7,
        choices=target_user_types.TARGET_USERS,
        default='all'
    )

    class Meta:

        ordering = ['-created_on']

    def __str__(self):
        return f'{self.name}'
