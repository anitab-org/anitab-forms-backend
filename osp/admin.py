from django.contrib import admin

from osp.models import (
    UserInformation, Form, Question, Choice,
    Checkbox, Dropdown, Paragraph, ShortAnswer,
    Date, Time, FileUpload, Answer, ChoiceValue,
    CheckboxValue, DropdownValue, ParagraphValue, ShortAnswerValue,
    DateValue, TimeValue, FileUploadValue, FormFeedback, ZulipStat
)

models = [
    UserInformation, Form, Question, Choice,
    Checkbox, Dropdown, Paragraph, ShortAnswer,
    Date, Time, FileUpload, Answer, ChoiceValue,
    CheckboxValue, DropdownValue, ParagraphValue, ShortAnswerValue,
    DateValue, TimeValue, FileUploadValue, FormFeedback, ZulipStat
]

admin.site.register(models)
