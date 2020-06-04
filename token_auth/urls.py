from django.urls import path, include

from token_auth.views.register import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view()),
]

