from rest_framework import serializers

from osp.models import (
    Question, Choice, Checkbox, Dropdown,
    Paragraph, ShortAnswer, Date, Time, FileUpload
)
from osp.serializers.question import QuestionSerializer

class ChoiceSerializer(QuestionSerializer):

    class Meta:

        model = Choice
        fields = QuestionSerializer.Meta.fields + ['options']

class CheckboxSerializer(QuestionSerializer):

    class Meta:

        model = Checkbox
        fields = QuestionSerializer.Meta.fields + ['options']

class DropdownSerializer(QuestionSerializer):

    class Meta:

        model = Dropdown
        fields = QuestionSerializer.Meta.fields + ['options']

class ParagraphSerializer(QuestionSerializer):

    class Meta:

        model = Paragraph
        fields = QuestionSerializer.Meta.fields

class ShortAnswerSerializer(QuestionSerializer):

    class Meta:

        model = ShortAnswer
        fields = QuestionSerializer.Meta.fields

class DateSerializer(QuestionSerializer):

    class Meta:

        model = Date
        fields = QuestionSerializer.Meta.fields

class TimeSerializer(QuestionSerializer):

    class Meta:

        model = Time
        fields = QuestionSerializer.Meta.fields

class FileUploadSerializer(QuestionSerializer):

    class Meta:

        model = FileUpload
        fields = QuestionSerializer.Meta.fields
