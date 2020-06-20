from django.db import models
from django.contrib.postgres.fields import ArrayField

from osp.models.question import Question

class Choice(Question):
    
    options = ArrayField(
        models.CharField(
            max_length=255,
            blank=True
        ))

class Dropdown(Question):
    
    options = ArrayField(
        models.CharField(
            max_length=255,
            blank=True
        ))

class Checkbox(Question):
    
    options = ArrayField(
        models.CharField(
            max_length=255,
            blank=True
        ))

class Paragraph(Question):
    pass

class ShortAnswer(Question):
    pass

class Date(Question):
    pass

class Time(Question):
    pass

class FileUpload(Question):
    pass