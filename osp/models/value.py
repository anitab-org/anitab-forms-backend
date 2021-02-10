from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

from osp.models.answer import Answer


class ChoiceValue(Answer):

    value = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.value


class DropdownValue(Answer):

    value = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.value


class CheckboxValue(Answer):

    value = ArrayField(models.CharField(max_length=255, blank=True))

    def __str__(self):
        return self.value


class ParagraphValue(Answer):

    value = models.TextField(blank=True)

    def __str__(self):
        return self.value


class ShortAnswerValue(Answer):

    value = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.value


class DateValue(Answer):

    value = models.DateField(default=timezone.now)

    def __str__(self):
        return self.value


class TimeValue(Answer):

    value = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.value


class FileUploadValue(Answer):

    value = models.TextField(blank=True)

    def __str__(self):
        return self.value
