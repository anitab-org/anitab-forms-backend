from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from osp.models import Form, UserInformation
from osp.permissions.admin import IsAdmin
from osp.serializers.form import FormSerializer


class FormView(viewsets.ModelViewSet):

    serializer_class = FormSerializer
    queryset = Form.objects.all()

    # override permissions for different request methods
    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsAdmin]

        return super(FormView, self).get_permissions()

    def get_queryset(self):
        queryset = self.queryset
        status = self.request.query_params.get("status", None)
        user = self.request.user
        user_type = UserInformation.objects.get(user_id=user.id).user_type
        if status:
            status = status.split(",")
            queryset = queryset.filter(published_status__in=status)
        if user_type == "student":
            queryset = queryset.filter(
                published_status__in=["published", "closed"], target_user__in=["all", "student"]
            )
        return queryset
