from django.db import models
from django.contrib.postgres.fields import ArrayField

from osp.models.question import Question

class Choice(Question):
    
    options = ArrayField(
        models.CharField(
            max_length=255,
            blank=True
        ))

    def __str__(self):
        return f'{self.label}'

class Dropdown(Question):
    
    options = ArrayField(
        models.CharField(
            max_length=255,
            blank=True
        ))

    def __str__(self):
        return f'{self.label}'

class Checkbox(Question):
    
    options = ArrayField(
        models.CharField(
            max_length=255,
            blank=True
        ))

    def __str__(self):
        return f'{self.label}'

class Paragraph(Question):

    def __str__(self):
        return f'{self.label}'

class ShortAnswer(Question):

    def __str__(self):
        return f'{self.label}'

class Date(Question):

    def __str__(self):
        return f'{self.label}'

class Time(Question):

    def __str__(self):
        return f'{self.label}'

class FileUpload(Question):

    def __str__(self):
        return f'{self.label}'
