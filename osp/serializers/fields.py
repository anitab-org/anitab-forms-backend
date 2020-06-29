from rest_framework import serializers

from osp.models import (
    Question, Choice, Checkbox, Dropdown,
    Paragraph, ShortAnswer, Date, Time, FileUpload
)
from osp.serializers.question import QuestionSerializer

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta(QuestionSerializer):

        model = Choice
        fields = QuestionSerializer.Meta.fields + ['options']

class CheckboxSerializer(serializers.ModelSerializer):

    class Meta(QuestionSerializer):

        model = Choice
        fields = QuestionSerializer.Meta.fields + ['options']

class DropdownSerializer(serializers.ModelSerializer):

    class Meta(QuestionSerializer):

        model = Choice
        fields = QuestionSerializer.Meta.fields + ['options']

class ParagraphSerializer(serializers.ModelSerializer):

    class Meta(QuestionSerializer):

        model = Choice
        fields = QuestionSerializer.Meta.fields

class ShortAnswerSerializer(serializers.ModelSerializer):

    class Meta(QuestionSerializer):

        model = Choice
        fields = QuestionSerializer.Meta.fields

class DateSerializer(serializers.ModelSerializer):

    class Meta(QuestionSerializer):

        model = Choice
        fields = QuestionSerializer.Meta.fields

class TimeSerializer(serializers.ModelSerializer):

    class Meta(QuestionSerializer):

        model = Choice
        fields = QuestionSerializer.Meta.fields

class FileUploadSerializer(serializers.ModelSerializer):

    class Meta(QuestionSerializer):

        model = Choice
        fields = QuestionSerializer.Meta.fields
