from django.db import models

from osp.models.question import Question
from osp.models.abstract_timestamp import AbstractTimestamp

ALL = 'all'
ADM = 'admin'
STU = 'student'
TARGET_USER = (
    (ALL, 'All Users'),
    (ADM, 'Admin'),
    (STU, 'Student'),
)

class Form(AbstractTimestamp):

    name = models.CharField(
        max_length=255
    )
    description = models.TextField(
        blank=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )
    published_status = models.BooleanField(
        default=False
    )
    form_fields = models.ManyToManyField(
        to=Question,
        default=None,
        blank=True,
    )
    target_user = models.CharField(
        max_length=7,
        choices=TARGET_USER,
        default='all'
    )

    def __str__(self):

        return f'{self.name}'