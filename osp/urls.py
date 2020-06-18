from django.urls import path, include
from rest_framework import routers

from osp.views.user import UserView
from osp.views.user_information import UserInformationView

router = routers.DefaultRouter()

router.register(r'user', UserView, basename='user')
router.register(r'info', UserInformationView, basename='information')


urlpatterns = [

]

urlpatterns +=router.urls

