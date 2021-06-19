from rest_framework import serializers

from osp.models import FormFeedback
from osp.serializers.form import FormSerializer
from osp.serializers.user import UserSerializer
from osp.utils.answer_function import get_model_and_serializer


class FormFeedbackReadSerializer(serializers.ModelSerializer):

    form = FormSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:

        model = FormFeedback
        fields = "__all__"

    def get_answers(self, obj):
        answers = []
        for answer in obj.answers.all():
            value = get_model_and_serializer(answer.question.data_type)
            serializer = value["serializer"]
            model = value["model"]
            instance = model.objects.get(id=answer.id)
            instance = serializer(instance)
            answers.append(instance.data)
        return answers


class FormFeedbackWriteSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:

        model = FormFeedback
        fields = "__all__"
