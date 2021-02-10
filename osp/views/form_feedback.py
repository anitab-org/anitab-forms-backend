from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import FormFeedback, Question
from osp.serializers.form_feedback import FormFeedbackReadSerializer, FormFeedbackWriteSerializer
from osp.utils.answer_function import get_create_model_and_serializer, get_model_and_serializer


class FormFeedbackView(viewsets.ModelViewSet):

    serializer_class = FormFeedbackReadSerializer
    permission_classes = [IsAuthenticated]
    queryset = FormFeedback.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        form_id = self.request.query_params.get("form_id", None)
        user_name = self.request.query_params.get("user_name", None)
        user_id = self.request.query_params.get("user_id", None)
        user = self.request.user
        if form_id is not None:
            form_id = form_id.split(",")
            queryset = queryset.filter(form_id__in=form_id)
        if user_name is not None:
            queryset = queryset.filter(
                Q(user__user_name__name__icontains=user_name) | Q(user__username__icontains=user_name)
            )
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        else:
            queryset = queryset.filter(user_id=user.id)

        # response
        return queryset

    # POST request
    def create(self, request):
        user = self.request.user
        answers = []

        for obj in request.data["answers"]:
            data_type = Question.objects.get(id=obj["question"]).data_type
            create_value = get_create_model_and_serializer(data_type)
            create_model = create_value["model"]
            create_serializer = create_value["serializer"]
            value = get_model_and_serializer(data_type)
            model = value["model"]
            serializer = value["serializer"]
            id = obj.get("id", None)
            if id is not None:
                instance = create_model.objects.get(id=id)
                instance = create_serializer(instance, data=obj)
                instance.is_valid(raise_exception=True)
                instance.save()
                obj = model.objects.get(id=instance.data["id"])
                instance = serializer(obj)
            else:
                instance = create_serializer(data=obj)
                instance.is_valid(raise_exception=True)
                instance.save()
                obj = model.objects.get(id=instance.data["id"])
                instance = serializer(obj)
            answers.append(instance.data["id"])

        request.data["answers"] = answers
        if FormFeedback.objects.filter(user_id=user.id).exists():
            instance = FormFeedback.objects.get(user_id=user.id)
            serializer = FormFeedbackWriteSerializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            serializer = FormFeedbackWriteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user_id=user.id)

        obj = FormFeedback.objects.get(id=serializer.data["id"])

        # response
        return Response(self.serializer_class(obj).data, status=status.HTTP_201_CREATED)
