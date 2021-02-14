from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient  
from rest_framework.test import APITestCase
import json

User = get_user_model()

class UserInfoTests(APITestCase):
    def setUp(self):

        # Needed for token auths
        self.client = APIClient()
        
        # Register
        self.register_data = {
            "username":"testuser1",
            "email":"testuser1@gmail.com",
            "password":"hello",
            "confirm_password":"hello"
        }
        test_user = User(username=self.register_data['username'],email=self.register_data['email'],is_active=True)
        test_user.set_password(self.register_data['password'])
        test_user.save()

        # Login and get real token
        login_data = {
            "username":self.register_data['username'],
            "password":self.register_data['password']
        }
        response = self.client.post('http://localhost:8000/api/token_auth/token/',login_data,format='json', headers={'Content-Type':'application/json'})
        self.access_token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
    
    def test_get_user_info_successfully_empty(self):

        response = self.client.get('http://localhost:8000/api/info/', format = 'json')
        self.assertEqual(response.data,[])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_user_info_successfully(self):
        
        body = {
            "name":"Test User 1 Full Name",
            "user_type":"admin",
            "zulip_id": 334084
        }
        response = self.client.post('http://localhost:8000/api/info/', body ,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user_info_successfully(self):

        response = self.client.get('http://localhost:8000/api/info/', format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_wrong_token(self):
        
        self.client.credentials()
        response = self.client.get('http://localhost:8000/api/info/', format = 'json')
        self.assertEqual(response.data['detail'],"Authentication credentials were not provided.")
        self.assertEqual(response.status_code, 403)

    def test_multiple_post_user_info(self):
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        body = {
            "name":"Test User 1 Full Name",
            "user_type":"admin",
            "zulip_id": 334084
        }
        for _ in range(2):
            response = self.client.post('http://localhost:8000/api/info/', body ,format = 'json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

