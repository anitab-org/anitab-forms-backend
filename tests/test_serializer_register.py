from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.serializers import ValidationError
from token_auth.serializers.register import RegisterSerializer

User = get_user_model()


class RegisterSerializerTests(TestCase):
    """
    Test for Register Serializer.
    """

    def setUp(self):
        self.test_user = self.__create_user("test", "test@test.com", "test")
        self.test_data = {
            'username': 'testuser2',
            'email': 'test2@test.com',
            'password': 'test',
            'confirm_password': 'test'
        }

    def __create_user(self, username, email, password):
        user = User(username=username, email=email, password=password)
        user.save()
        return user

    def test_get_serializer(self):
        """
        Testing Response of Register Serializer.
        """
        actual_response = RegisterSerializer(self.test_user).data
        expected_response = {
            'username': self.test_user.username,
            'email': self.test_user.email
        }
        self.assertEqual(actual_response, expected_response)

    def test_create_serializer(self):
        """
        Testing create method of Register Serializer.
        """
        serializer = RegisterSerializer(data=self.test_data)
        if serializer.is_valid():
            user = serializer.save()
        self.assertEquals(user, User.objects.get(
            email=self.test_data['email']))

    def test_create_serializer_with_same_email_id(self):
        """
        Testing Validation Error in create method of Register Serializer
        when a user with same email-id exists.
        """
        serializer = RegisterSerializer(data=self.test_user.__dict__)
        if serializer.is_valid():
            with self.assertRaises(ValidationError):
                serializer.save()

    def test_create_serializer_with_different_passwords(self):
        """
        Testing Validation Error in create method of Register Serializer
        when password and confirm password are not equal.
        """
        self.test_data['password'] = 'different'
        serializer = RegisterSerializer(data=self.test_data)
        if serializer.is_valid():
            with self.assertRaises(ValidationError):
                serializer.save()
