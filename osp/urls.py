from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from osp.views.user import UserView
from osp.views.user_information import UserInformationView
from osp.views.form import FormView
from osp.views.question import QuestionView

router = routers.DefaultRouter()

router.register(r'user', UserView, basename='user')
router.register(r'info', UserInformationView, basename='information')
router.register(r'form', FormView, basename='form')
router.register(r'questions', QuestionView, basename='questions')

urlpatterns = [
]

urlpatterns +=router.urls

