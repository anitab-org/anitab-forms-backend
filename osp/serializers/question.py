from rest_framework import serializers

from osp.models import Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question
        fields = [
            'id', 'label', 'data_type', 'description', 'order', 'required',
            'created_on', 'updated_on', 'forms'
        ]
