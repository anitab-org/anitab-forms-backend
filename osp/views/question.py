from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import (
    UserInformation, Form, Question, Choice,
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
    queryset = Question.objects.all()

    # override permissions for different request methods
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsAdmin]

        return super(QuestionView, self).get_permissions()
    
    def get_queryset(self):
        queryset = self.queryset
        form_id = self.request.query_params.get('form_id', None)
        user = self.request.user
        user_type = UserInformation.objects.get(id=user.id).user_type
        if form_id:
            queryset = queryset.filter(forms__id=form_id)
        if user_type == 'student':
            queryset = queryset.filter(forms__published_status='published')
        return queryset
    
    # GET request
    def list(self, request):
        objs = self.get_queryset()
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
        results = []

        for obj in request.data:
            value = get_model_and_serializer(obj['data_type'])
            model = value['model']
            serializer = value['serializer']
            id = obj.get('id', None)
            if id is not None:
                instance = model.objects.get(id=id)
                instance = serializer(instance, data=obj)
                instance.is_valid(raise_exception=True)
                instance.save()
            else:
                instance = serializer(data=obj)
                instance.is_valid(raise_exception=True)
                instance.save()
            results.append(instance.data)

        # response
        return Response(results, status=status.HTTP_201_CREATED)

