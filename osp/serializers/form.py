from rest_framework import serializers

from osp.models import Form

class FormSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Form
        fields = [
            'id', 'name', 'description', 'published_status',
            'questions', 'target_user', 'created_on', 'updated_on'
        ]
