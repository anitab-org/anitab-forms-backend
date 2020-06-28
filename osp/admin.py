from django.contrib import admin

from osp.models import (
    UserInformation, Form, Question, Choice,
    Checkbox, Dropdown, Paragraph, ShortAnswer,
    Date, Time, FileUpload
)

models = [
    UserInformation, Form, Question, Choice,
    Checkbox, Dropdown, Paragraph, ShortAnswer,
    Date, Time, FileUpload
]

admin.site.register(models)
