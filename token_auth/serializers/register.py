from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.serializers import PasswordField

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    password = PasswordField(
        write_only=True,
        required=True
    )
    confirm_password = PasswordField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "confirm_password",
        ]

    def create(self, validated_data):

        username = validated_data.get('username', None)
        email = validated_data.get('email', None)
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if (email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError("Email addresses must be unique.")

        if password != confirm_password:
            raise serializers.ValidationError("The two passwords differ.")

        user = User(username=username, email=email)
        user.set_password(password)
        user.is_active = False
        user.save()

        return user
    
