from rest_framework import serializers

from osp.models import Answer
from osp.serializers.question import QuestionSerializer

class AnswerReadSerializer(serializers.ModelSerializer):

    question = QuestionSerializer(read_only=True)

    class Meta:

        model = Answer
        fields = [
            'id', 'question', 'created_on', 'updated_on'
        ]

class AnswerWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id', 'question', 'created_on', 'updated_on'
        ]
