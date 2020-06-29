from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from osp.views.user import UserView
from osp.views.user_information import UserInformationView
from osp.views.unpublished_form import UnpublishedFormView
from osp.views.published_form import PublishedFormView
from osp.views.question import QuestionView

router = routers.DefaultRouter()

router.register(r'user', UserView, basename='user')
router.register(r'info', UserInformationView, basename='information')
router.register(r'unpublished_form', UnpublishedFormView, basename='unpublished_form')
router.register(r'published_form', PublishedFormView, basename='published_form')
# router.register(r'questions', QuestionView, basename='questions')

urlpatterns = [
    url(r'questions/(?P<form_id>\d+)/$', QuestionView.as_view({
        'get': 'list'
    })),
]

urlpatterns +=router.urls

