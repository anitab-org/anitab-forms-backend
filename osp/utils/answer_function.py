from rest_framework.response import Response

from osp.models import (
    ChoiceValue, CheckboxValue, DropdownValue, ParagraphValue,
    ShortAnswerValue, DateValue, TimeValue, FileUploadValue
)
from osp.serializers.value import (
    ChoiceValueReadSerializer, ChoiceValueWriteSerializer, CheckboxValueReadSerializer, CheckboxValueWriteSerializer,
    DropdownValueReadSerializer, DropdownValueWriteSerializer, ParagraphValueReadSerializer, ParagraphValueWriteSerializer,
    ShortAnswerValueReadSerializer, ShortAnswerValueWriteSerializer, DateValueReadSerializer, DateValueWriteSerializer,
    TimeValueReadSerializer, TimeValueWriteSerializer, FileUploadValueReadSerializer, FileUploadValueWriteSerializer
)

def get_create_model_and_serializer(data_type):
    if data_type == 'char':
        model = ShortAnswerValue
        serializer = ShortAnswerValueWriteSerializer

    elif data_type == 'text':
        model = ParagraphValue
        serializer = ParagraphValueWriteSerializer

    elif data_type == 'choice':
        model = ChoiceValue
        serializer = ChoiceValueWriteSerializer

    elif data_type == 'checkbox':
        model = CheckboxValue
        serializer = CheckboxValueWriteSerializer

    elif data_type == 'dropdown':
        model = DropdownValue
        serializer = DropdownValueWriteSerializer

    elif data_type == 'date':
        model = DateValue
        serializer = DateValueWriteSerializer

    elif data_type == 'time':
        model = TimeValue
        serializer = TimeValueWriteSerializer

    elif data_type == 'file':
        model = FileUploadValue
        serializer = FileUploadValueWriteSerializer

    return {
        "model": model,
        "serializer": serializer
    }

def get_model_and_serializer(data_type):
    if data_type == 'char':
        model = ShortAnswerValue
        serializer = ShortAnswerValueReadSerializer

    elif data_type == 'text':
        model = ParagraphValue
        serializer = ParagraphValueReadSerializer

    elif data_type == 'choice':
        model = ChoiceValue
        serializer = ChoiceValueReadSerializer

    elif data_type == 'checkbox':
        model = CheckboxValue
        serializer = CheckboxValueReadSerializer

    elif data_type == 'dropdown':
        model = DropdownValue
        serializer = DropdownValueReadSerializer

    elif data_type == 'date':
        model = DateValue
        serializer = DateValueReadSerializer

    elif data_type == 'time':
        model = TimeValue
        serializer = TimeValueReadSerializer

    elif data_type == 'file':
        model = FileUploadValue
        serializer = FileUploadValueReadSerializer

    return {
        "model": model,
        "serializer": serializer
    }

