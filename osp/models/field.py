from django.db import models
from django.contrib.postgres.fields import ArrayField

from osp.models.utils.question import Question

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

        return '{self.label}'

class Checkbox(Question):
    
    options = ArrayField(
        models.CharField(
            max_length=255,
            blank=True
        ))

    def __str__(self):

        return '{self.label}'

class Paragraph(Question):
    pass

    def __str__(self):

        return '{self.label}'

class ShortAnswer(Question):
    pass

    def __str__(self):

        return '{self.label}'

class Date(Question):
    pass

    def __str__(self):

        return '{self.label}'

class Time(Question):
    pass

    def __str__(self):

        return '{self.label}'

class FileUpload(Question):
    pass

    def __str__(self):

        return '{self.label}'
