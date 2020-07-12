from rest_framework import serializers

from osp.models import (
    Answer, ChoiceValue, CheckboxValue, DropdownValue,
    ParagraphValue, ShortAnswerValue, DateValue, TimeValue, FileUploadValue
)
from osp.serializers.answer import AnswerReadSerializer, AnswerWriteSerializer

# read serializers
class ChoiceValueReadSerializer(AnswerReadSerializer):

    class Meta:

        model = ChoiceValue
        fields = AnswerReadSerializer.Meta.fields + ['value']

class CheckboxValueReadSerializer(AnswerReadSerializer):

    class Meta:

        model = CheckboxValue
        fields = AnswerReadSerializer.Meta.fields + ['value']

class DropdownValueReadSerializer(AnswerReadSerializer):

    class Meta:

        model = DropdownValue
        fields = AnswerReadSerializer.Meta.fields + ['value']

class ParagraphValueReadSerializer(AnswerReadSerializer):

    class Meta:

        model = ParagraphValue
        fields = AnswerReadSerializer.Meta.fields + ['value']

class ShortAnswerValueReadSerializer(AnswerReadSerializer):

    class Meta:

        model = ShortAnswerValue
        fields = AnswerReadSerializer.Meta.fields + ['value']

class DateValueReadSerializer(AnswerReadSerializer):

    class Meta:

        model = DateValue
        fields = AnswerReadSerializer.Meta.fields + ['value']

class TimeValueReadSerializer(AnswerReadSerializer):

    class Meta:

        model = TimeValue
        fields = AnswerReadSerializer.Meta.fields + ['value']

class FileUploadValueReadSerializer(AnswerReadSerializer):

    class Meta:

        model = FileUploadValue
        fields = AnswerReadSerializer.Meta.fields + ['value']

# write serializers
class ChoiceValueWriteSerializer(AnswerWriteSerializer):

    class Meta:

        model = ChoiceValue
        fields = AnswerWriteSerializer.Meta.fields + ['value']

class CheckboxValueWriteSerializer(AnswerWriteSerializer):

    class Meta:

        model = CheckboxValue
        fields = AnswerWriteSerializer.Meta.fields + ['value']

class DropdownValueWriteSerializer(AnswerWriteSerializer):

    class Meta:

        model = DropdownValue
        fields = AnswerWriteSerializer.Meta.fields + ['value']

class ParagraphValueWriteSerializer(AnswerWriteSerializer):

    class Meta:

        model = ParagraphValue
        fields = AnswerWriteSerializer.Meta.fields + ['value']

class ShortAnswerValueWriteSerializer(AnswerWriteSerializer):

    class Meta:

        model = ShortAnswerValue
        fields = AnswerWriteSerializer.Meta.fields + ['value']

class DateValueWriteSerializer(AnswerWriteSerializer):

    class Meta:

        model = DateValue
        fields = AnswerWriteSerializer.Meta.fields + ['value']

class TimeValueWriteSerializer(AnswerWriteSerializer):

    class Meta:

        model = TimeValue
        fields = AnswerWriteSerializer.Meta.fields + ['value']

class FileUploadValueWriteSerializer(AnswerWriteSerializer):

    class Meta:

        model = FileUploadValue
        fields = AnswerWriteSerializer.Meta.fields + ['value']
