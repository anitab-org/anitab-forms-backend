from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import Form
from osp.serializers.form import FormSerializer

class PublishedFormView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = FormSerializer

    def get_queryset(self):
        queryset = Form.objects.filter(published_status=True)
        return queryset
