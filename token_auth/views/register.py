from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from token_auth.serializers.register import RegisterSerializer
from token_auth.views.token import account_activation_token

User = get_user_model()


@permission_classes([AllowAny])
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Function for creating user account
        """

        # Account Creation
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        url = f"{urlsafe_base64_encode(force_bytes(user.pk))}/{account_activation_token.make_token(user)}"
        # Send Email for confirmation
        send_mail(
            "Confirmation Email",
            f"Please click on the link to confirm the link: http://localhost:3000/{url} ",
            "AnitaB Open Source <opensource@anitab.org>",
            [request.data["email"]],
            fail_silently=False,
        )
        return Response({"Please confirm your email to Login succesfully"}, status.HTTP_201_CREATED)

    @api_view(("GET",))
    @permission_classes([AllowAny])
    def activate(request, uidb64, token):
        """
        Function for account activation
        """

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"Your email is confirmed!"}, status=status.HTTP_200_OK)
        else:
            return Response({"Invalid link"}, status=status.HTTP_400_BAD_REQUEST)
