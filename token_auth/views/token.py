from django.contrib.auth.tokens import PasswordResetTokenGenerator

# from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):

    """
    Class for generation token for email confirmation
    """

    def _make_hash_value(self, user, timestamp):

        return str(user.pk) + str(timestamp) + str(user.is_active)


account_activation_token = TokenGenerator()
