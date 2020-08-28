from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import UserInformation
from osp.serializers.user_information import UserInformationSerializer
from osp.utils.zulip_api import get_zulip_user

class UserInformationView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated, ]
    serializer_class = UserInformationSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UserInformation.objects.filter(user_id=user.id)
        return queryset

    def create(self, request):
        user = self.request.user
        serializer = UserInformationSerializer(data=request.data)
        if UserInformation.objects.filter(user_id=user.id).exists():
            return Response("Information already filled", status=status.HTTP_409_CONFLICT)
        response = get_zulip_user(request.data['zulip_id'])
        result = response.get('result', None)
        if result is not None and result=='success':
            serializer.is_valid(raise_exception=True)
            serializer.save(user_id=user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response("No user found with the Zulip ID entered.", status=status.HTTP_404_NOT_FOUND)
