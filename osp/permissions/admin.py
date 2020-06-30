from rest_framework import permissions

from osp.models import UserInformation

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        user_type = UserInformation.objects.get(user_id=user.id).user_type
        return user_type == 'admin'
