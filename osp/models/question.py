from django.db import models

from osp.models.abstract_timestamp import AbstractTimestamp

SA = 'char'
PA = 'text'
CF = 'choice'
CH = 'checkbox'
DD = 'dropdown'
FI = 'file'
DA = 'date'
TI = 'time'
DATA_TYPE = (
    (SA, 'Short Answer'),
    (PA, 'Paragraph Answer'),
    (CF, 'Choice'),
    (CH, 'Checkbox'),
    (DD, 'Dropdown'),
    (FI, 'File Upload'),
    (DA, 'Date'),
    (TI, 'Time')
)

class Question(AbstractTimestamp):

    label = models.CharField(max_length=255)
    data_type = models.CharField(
        max_length=8,
        choices=DATA_TYPE
    )
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField()
    required = models.BooleanField(default=False)
