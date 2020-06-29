from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import Form, Question
from osp.serializers.question import QuestionSerializer
from osp.serializers.fields import (
    ChoiceSerializer, CheckboxSerializer, DropdownSerializer,
    ParagraphSerializer, ShortAnswerSerializer, ParagraphSerializer,
    DateSerializer, TimeSerializer, FileUploadSerializer
)

class QuestionView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        request_arg = self.kwargs.get('form_id', '')
        queryset = Form.objects.get(id=request_arg).form_fields
        return queryset
