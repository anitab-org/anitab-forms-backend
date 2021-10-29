import json

import responses
from allauth.socialaccount.models import SocialApp
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TestGoogleAuth(TestCase):
    """
    Tests for Google Authentication !!
    """

    def setUp(self):
        self.client = APIClient()
        self.google_signup_url = reverse("google_login")
        self.payload = {"access_token": "1234567", "id_token": "789456123"}
        social_app = SocialApp.objects.create(
            provider="google",
            name="Google",
            client_id="123456123456123456654321",
            secret="654321123456123456987456123",
        )
        site = Site.objects.get_current()
        social_app.sites.add(site)
        
    @responses.activate
    def test_google_auth(self):
        """
        Testing Google Auth SignUp !!
        """
        self._get_google_response()
        user_count = get_user_model().objects.all().count()

        response = self.client.post(self.google_signup_url, data=self.payload, format="json")
        self.assertEquals(response.status_code, 200)
        # assertion to check new user is created.
        self.assertEquals(get_user_model().objects.all().count(), user_count + 1)

        # Below two assertions are added to check REST_USE_JWT is True or not.
        self.assertIn("access_token", response.data)
        self.assertIn("refresh_token", response.data)

        # Assertion to check second request will not create a new user
        response = self.client.post(self.google_signup_url, data=self.payload, format="json")

        self.assertEquals(get_user_model().objects.all().count(), user_count + 1)

    def _get_google_response(self):
        """
        Private methods to get response from Google API Calls.
        """

        responses.add(
            responses.POST,
            "https://accounts.google.com/o/oauth2/v2/auth",
            body=json.dumps({"access_token": "access_token", "id_token": "id_token"}),
            status=200,
            content_type="application/json",
        )

        responses.add(
            responses.GET,
            "https://www.googleapis.com/oauth2/v2/userinfo",
            body=json.dumps(
                {
                    "id": "456123",
                    "email": "testuser@gmail.com",
                    "picture": "https://lh3.googleusercontent.com/a-/saf456fq1fc894veqw1fsc2",
                    "type": "User",
                    "verified_email": "true",
                }
            ),
            status=200,
            content_type="application/json",
        )
