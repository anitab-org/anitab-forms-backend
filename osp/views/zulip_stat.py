from datetime import datetime

from django.utils.timezone import make_aware
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from osp.models import UserInformation, ZulipStat
from osp.serializers.zulip_stat import ZulipStatSerializer
from osp.serializers.zulip_stat_user import ZulipStatUserSerializer
from osp.utils.zulip_api import get_messages, get_newest_message, get_stream_messages, get_zulip_user


class ZulipStatView(viewsets.ModelViewSet):

    permission_classes = [
        IsAuthenticated,
    ]
    queryset = ZulipStat.objects.all()

    def get_serializer_class(self):
        user = self.request.user
        user_type = UserInformation.objects.get(user=user.id).user_type
        if user_type == "admin":
            self.serializer_class = ZulipStatSerializer
        else:
            self.serializer_class = ZulipStatUserSerializer
        return super(ZulipStatView, self).get_serializer_class()

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        user_id = self.request.query_params.get("user_id", None)
        if user_id is not None:
            queryset = queryset.filter(user_information__user_id=user_id)
        else:
            queryset = queryset.filter(user_information__user_id=user.id)
        return queryset

    def create(self, request):
        user = self.request.user
        user_info = UserInformation.objects.get(user_id=user.id)

        # update on existing
        if ZulipStat.objects.filter(user_information__user_id=user.id).exists():
            zulip_id = user_info.zulip_id
            zulip_user = get_zulip_user(zulip_id)
            for z in zulip_user:
                if z == "full_name":
                    full_name = zulip_user[z]

            recent_message = get_newest_message(zulip_id)
            for r in recent_message:
                last_activity = r["timestamp"]

            request.data["zulip_username"] = full_name
            request.data["total_messages"] = get_messages(zulip_id)
            request.data["last_activity"] = make_aware(datetime.fromtimestamp(last_activity))
            request.data["newcomers_messages"] = get_stream_messages("newcomers", zulip_id)
            request.data["general_messages"] = get_stream_messages("general", zulip_id)
            request.data["questions_messages"] = get_stream_messages("questions", zulip_id)
            request.data["opportunities_messages"] = get_stream_messages("opportunities", zulip_id)
            request.data["celebrate_messages"] = get_stream_messages("celebrate", zulip_id)

            instance = ZulipStat.objects.get(user_information_id=user_info.id)
            serializer = ZulipStatSerializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        # create if field does not exist
        else:
            zulip_id = user_info.zulip_id
            zulip_user = get_zulip_user(zulip_id)
            for z in zulip_user:
                if z == "full_name":
                    full_name = zulip_user[z]
                if z == "date_joined":
                    first_activity = zulip_user[z]

            recent_message = get_newest_message(zulip_id)
            for r in recent_message:
                last_activity = r["timestamp"]

            request.data["zulip_username"] = full_name
            request.data["total_messages"] = get_messages(zulip_id)
            request.data["last_activity"] = make_aware(datetime.fromtimestamp(last_activity))
            request.data["first_activity"] = first_activity
            request.data["newcomers_messages"] = get_stream_messages("newcomers", zulip_id)
            request.data["general_messages"] = get_stream_messages("general", zulip_id)
            request.data["questions_messages"] = get_stream_messages("questions", zulip_id)
            request.data["opportunities_messages"] = get_stream_messages("opportunities", zulip_id)
            request.data["celebrate_messages"] = get_stream_messages("celebrate", zulip_id)

            serializer = ZulipStatSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user_information_id=user_info.id)

        obj = ZulipStat.objects.get(id=serializer.data["id"])
        self.get_serializer_class()

        # response
        return Response(self.serializer_class(obj).data, status=status.HTTP_201_CREATED)
