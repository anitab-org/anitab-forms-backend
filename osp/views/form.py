from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import Form
from osp.serializers.form import FormSerializer
from osp.permissions.admin import IsAdmin

class FormView(viewsets.ModelViewSet):

    serializer_class = FormSerializer

    # override permissions for different request methods
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsAdmin]

        return super(FormView, self).get_permissions()

    def get_queryset(self):
        status = self.request.query_params.get('status', None)
        queryset = Form.objects.filter(published_status=status).order_by('-created_on')
        return queryset
