from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from token_auth.views.register import RegisterView
from token_auth.views.login import LoginView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', RegisterView.activate, name='activate'),

    # login URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

