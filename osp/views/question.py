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
        char = []
        text = []
        choice = []
        checkbox = []
        dropdown = []
        date = []
        time = []
        file_upload = []

        # loop for retrieving all objects
        for obj in objs:
            if obj.data_type == 'char':
                char.append(ShortAnswer.objects.get(id=obj.id))

            elif obj.data_type == 'text':
                text.append(Paragraph.objects.get(id=obj.id))

            elif obj.data_type == 'choice':
                choice.append(Choice.objects.get(id=obj.id))

            elif obj.data_type == 'checkbox':
                checkbox.append(Checkbox.objects.get(id=obj.id))

            elif obj.data_type == 'dropdown':
                dropdown.append(Dropdown.objects.get(id=obj.id))

            elif obj.data_type == 'date':
                date.append(Date.objects.get(id=obj.id))

            elif obj.data_type == 'time':
                time.append(Time.objects.get(id=obj.id))

            elif obj.data_type == 'file':
                file_upload.append(FileUpload.objects.get(id=obj.id))

        # serializing the objects
        char_serializer = ShortAnswerSerializer(char, many=True)
        text_serializer = ParagraphSerializer(text, many=True)
        choice_serializer = ChoiceSerializer(choice, many=True)
        checkbox_serializer = CheckboxSerializer(checkbox, many=True)
        dropdown_serializer = DropdownSerializer(dropdown, many=True)
        date_serializer = DateSerializer(date, many=True)
        time_serializer = TimeSerializer(time, many=True)
        file_serializer = FileUploadSerializer(file_upload, many=True)
            
        #response
        return Response((
            char_serializer.data, text_serializer.data,
            choice_serializer.data, checkbox_serializer.data,
            dropdown_serializer.data, date_serializer.data,
            time_serializer.data, file_serializer.data
        ), status=status.HTTP_200_OK)


    # POST request
    def create(self, request):
        form_id = self.request.query_params.get('form_id', None)
        form = Form.objects.get(id=form_id)
        char = []
        text = []
        choice = []
        checkbox = []
        dropdown = []
        date = []
        time = []
        file_upload = []

        # loop for creating objects
        for obj in request.data:
            if obj['data_type'] == 'char':
                instance = ShortAnswer.objects.create(
                        label=obj['label'],
                        data_type=obj['data_type'],
                        description=obj['description'],
                        order=obj['order'],
                        required=obj['required']
                    )
                char.append(instance)
                form.form_fields.add(instance)

            elif obj['data_type'] == 'text':
                instance = Paragraph.objects.create(
                        label=obj['label'],
                        data_type=obj['data_type'],
                        description=obj['description'],
                        order=obj['order'],
                        required=obj['required']
                    ) 
                text.append(instance)
                form.form_fields.add(instance)

            elif obj['data_type'] == 'choice':
                instance = Choice.objects.create(
                        label=obj['label'],
                        data_type=obj['data_type'],
                        description=obj['description'],
                        order=obj['order'],
                        required=obj['required'],
                        options=obj['options']
                    )
                choice.append(instance)
                form.form_fields.add(instance)

            elif obj['data_type'] == 'checkbox':
                instance = Checkbox.objects.create(
                        label=obj['label'],
                        data_type=obj['data_type'],
                        description=obj['description'],
                        order=obj['order'],
                        required=obj['required'],
                        options=obj['options']
                    )
                checkbox.append(instance)
                form.form_fields.add(instance)

            elif obj['data_type'] == 'dropdown':
                instance = Dropdown.objects.create(
                        label=obj['label'],
                        data_type=obj['data_type'],
                        description=obj['description'],
                        order=obj['order'],
                        required=obj['required'],
                        options=obj['options']
                    )
                dropdown.append(instance)
                form.form_fields.add(instance)

            elif obj['data_type'] == 'date':
                instance = Date.objects.create(
                        label=obj['label'],
                        data_type=obj['data_type'],
                        description=obj['description'],
                        order=obj['order'],
                        required=obj['required']
                    )
                date.append(instance)
                form.form_fields.add(instance)

            elif obj['data_type'] == 'time':
                instance = Time.objects.create(
                        label=obj['label'],
                        data_type=obj['data_type'],
                        description=obj['description'],
                        order=obj['order'],
                        required=obj['required']
                    )
                time.append(instance)
                form.form_fields.add(instance)

            elif obj['data_type'] == 'file':
                instance = FileUpload.objects.create(
                        label=obj['label'],
                        data_type=obj['data_type'],
                        description=obj['description'],
                        order=obj['order'],
                        required=obj['required']
                    )
                file_upload.append(instance)
                form.form_fields.add(instance)


        # serializing the objects
        char_serializer = ShortAnswerSerializer(char, many=True)
        text_serializer = ParagraphSerializer(text, many=True)
        choice_serializer = ChoiceSerializer(choice, many=True)
        checkbox_serializer = CheckboxSerializer(checkbox, many=True)
        dropdown_serializer = DropdownSerializer(dropdown, many=True)
        date_serializer = DateSerializer(date, many=True)
        time_serializer = TimeSerializer(time, many=True)
        file_serializer = FileUploadSerializer(file_upload, many=True)

        # response
        return Response((
            char_serializer.data, text_serializer.data,
            choice_serializer.data, checkbox_serializer.data,
            dropdown_serializer.data, date_serializer.data,
            time_serializer.data, file_serializer.data
        ), status=status.HTTP_201_CREATED)

