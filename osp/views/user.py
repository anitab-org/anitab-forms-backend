from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.serializers.user import UserSerializer

User = get_user_model()

class UserView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(id=user.id)
        return queryset

