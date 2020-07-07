from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import (
    Form, Question, Choice,
    Checkbox, Dropdown, Paragraph, ShortAnswer,
    Date, Time, FileUpload
)
from osp.serializers.question import QuestionSerializer
from osp.serializers.fields import (
    ChoiceSerializer, CheckboxSerializer, DropdownSerializer,
    ParagraphSerializer, ShortAnswerSerializer, ParagraphSerializer,
    DateSerializer, TimeSerializer, FileUploadSerializer
)
from osp.permissions.admin import IsAdmin
from osp.utils.question import get_model_and_serializer

class QuestionView(viewsets.ViewSet):

    serializer_class = QuestionSerializer

    # override permissions for different request methods
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsAdmin]

        return super(QuestionView, self).get_permissions()

    
    # GET request
    def list(self, request):
        form_id = self.request.query_params.get('form_id', None)
        fields = Form.objects.filter(id=form_id).values_list('form_fields', flat=True)
        objs = Question.objects.filter(id__in=fields)
        results = []

        for obj in objs:
            value = get_model_and_serializer(obj.data_type)
            model = value['model']
            serializer = value['serializer']
            instance = model.objects.get(id=obj.id)
            results.append(serializer(instance).data)
            
        #response
        return Response(results, status=status.HTTP_200_OK)


    # POST request
    def create(self, request):
        form_id = self.request.query_params.get('form_id', None)
        form = Form.objects.get(id=form_id)
        results = []

        for obj in request.data:
            value = get_model_and_serializer(obj['data_type'])
            model = value['model']
            serializer = value['serializer']
            id = obj.get('id', None)
            if id is not None:
                model.objects.filter(id=id).update(**obj)
                instance = model.objects.get(id=id)
            else:
                instance = model.objects.create(**obj)
            results.append(serializer(instance).data)
            form.form_fields.add(instance)

        # response
        return Response(results, status=status.HTTP_201_CREATED)

