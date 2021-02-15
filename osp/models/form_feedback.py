from django.conf import settings
from django.db import models

from osp.models.answer import Answer
from osp.models.form import Form
from osp.utils import choices


class FormFeedback(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    answers = models.ManyToManyField(to=Answer, default=None, blank=True, related_name="form_answers")
    acceptance_status = models.CharField(max_length=10, choices=choices.ACCEPTANCE_STATUSES, default="pending")
