from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import Answer
from osp.serializers.answer import AnswerReadSerializer
from osp.utils.answer_function import get_model_and_serializer


class AnswerView(viewsets.ModelViewSet):

    serializer_class = AnswerReadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all().order_by("question__order")

    def get_queryset(self):
        queryset = self.queryset
        form_id = self.request.query_params.get("form_id", None)
        question_id = self.request.query_params.get("question_id", None)
        user_id = self.request.query_params.get("user_id", None)
        user = self.request.user
        if form_id is not None:
            queryset = queryset.filter(form_answers__form_id=form_id)
        if user_id is not None:
            queryset = queryset.filter(form_answers__user_id=user_id)
        else:
            queryset = queryset.filter(form_answers__user_id=user.id)
        if question_id is not None:
            queryset = queryset.filter(question_id=question_id)

        # response
        return queryset

    # GET request
    def list(self, request):
        objs = self.get_queryset()
        results = []

        for obj in objs:
            value = get_model_and_serializer(obj.question.data_type)
            model = value["model"]
            serializer = value["serializer"]
            instance = model.objects.get(id=obj.id)
            results.append(serializer(instance).data)

        # response
        return Response(results, status=status.HTTP_200_OK)
