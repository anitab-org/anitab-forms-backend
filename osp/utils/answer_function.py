from osp.models import (
    CheckboxValue,
    ChoiceValue,
    DateValue,
    DropdownValue,
    FileUploadValue,
    ParagraphValue,
    ShortAnswerValue,
    TimeValue,
)
from osp.serializers.value import (
    CheckboxValueReadSerializer,
    CheckboxValueWriteSerializer,
    ChoiceValueReadSerializer,
    ChoiceValueWriteSerializer,
    DateValueReadSerializer,
    DateValueWriteSerializer,
    DropdownValueReadSerializer,
    DropdownValueWriteSerializer,
    FileUploadValueReadSerializer,
    FileUploadValueWriteSerializer,
    ParagraphValueReadSerializer,
    ParagraphValueWriteSerializer,
    ShortAnswerValueReadSerializer,
    ShortAnswerValueWriteSerializer,
    TimeValueReadSerializer,
    TimeValueWriteSerializer,
)


def get_create_model_and_serializer(data_type):
    if data_type == "char":
        model = ShortAnswerValue
        serializer = ShortAnswerValueWriteSerializer

    elif data_type == "text":
        model = ParagraphValue
        serializer = ParagraphValueWriteSerializer

    elif data_type == "choice":
        model = ChoiceValue
        serializer = ChoiceValueWriteSerializer

    elif data_type == "checkbox":
        model = CheckboxValue
        serializer = CheckboxValueWriteSerializer

    elif data_type == "dropdown":
        model = DropdownValue
        serializer = DropdownValueWriteSerializer

    elif data_type == "date":
        model = DateValue
        serializer = DateValueWriteSerializer

    elif data_type == "time":
        model = TimeValue
        serializer = TimeValueWriteSerializer

    elif data_type == "file":
        model = FileUploadValue
        serializer = FileUploadValueWriteSerializer

    return {"model": model, "serializer": serializer}


def get_model_and_serializer(data_type):
    if data_type == "char":
        model = ShortAnswerValue
        serializer = ShortAnswerValueReadSerializer

    elif data_type == "text":
        model = ParagraphValue
        serializer = ParagraphValueReadSerializer

    elif data_type == "choice":
        model = ChoiceValue
        serializer = ChoiceValueReadSerializer

    elif data_type == "checkbox":
        model = CheckboxValue
        serializer = CheckboxValueReadSerializer

    elif data_type == "dropdown":
        model = DropdownValue
        serializer = DropdownValueReadSerializer

    elif data_type == "date":
        model = DateValue
        serializer = DateValueReadSerializer

    elif data_type == "time":
        model = TimeValue
        serializer = TimeValueReadSerializer

    elif data_type == "file":
        model = FileUploadValue
        serializer = FileUploadValueReadSerializer

    return {"model": model, "serializer": serializer}
