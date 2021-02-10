from osp.models import Checkbox, Choice, Date, Dropdown, FileUpload, Paragraph, ShortAnswer, Time
from osp.serializers.fields import (
    CheckboxSerializer,
    ChoiceSerializer,
    DateSerializer,
    DropdownSerializer,
    FileUploadSerializer,
    ParagraphSerializer,
    ShortAnswerSerializer,
    TimeSerializer,
)


def get_model_and_serializer(data_type):
    if data_type == "char":
        model = ShortAnswer
        serializer = ShortAnswerSerializer

    elif data_type == "text":
        model = Paragraph
        serializer = ParagraphSerializer

    elif data_type == "choice":
        model = Choice
        serializer = ChoiceSerializer

    elif data_type == "checkbox":
        model = Checkbox
        serializer = CheckboxSerializer

    elif data_type == "dropdown":
        model = Dropdown
        serializer = DropdownSerializer

    elif data_type == "date":
        model = Date
        serializer = DateSerializer

    elif data_type == "time":
        model = Time
        serializer = TimeSerializer

    elif data_type == "file":
        model = FileUpload
        serializer = FileUploadSerializer

    return {"model": model, "serializer": serializer}
