from rest_framework import serializers

from osp.models import ZulipStat


class ZulipStatSerializer(serializers.ModelSerializer):

    zulip_user_id = serializers.CharField(source="user_information.zulip_id", read_only=True)

    class Meta:

        model = ZulipStat
        fields = [
            "id",
            "zulip_user_id",
            "zulip_username",
            "total_messages",
            "first_activity",
            "last_activity",
            "updated_on",
            "newcomers_messages",
            "general_messages",
            "questions_messages",
            "opportunities_messages",
            "celebrate_messages",
        ]
