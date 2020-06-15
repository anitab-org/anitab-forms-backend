from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from token_auth.views.register import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    url(r'^activate/(?P<user_id>\d+)/$', RegisterView.activate, name='activate'),

    # login URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

