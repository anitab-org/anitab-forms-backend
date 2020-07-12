from django.db import models

from osp.models.abstract_timestamp import AbstractTimestamp
from osp.models.question import Question

class Answer(AbstractTimestamp):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
