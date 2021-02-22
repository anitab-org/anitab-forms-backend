from django.conf import settings
from django.test import TestCase


class TestConfig(TestCase):
    def test_config(self):
        self.assertIsNotNone(settings.SECRET_KEY)
        self.assertNotEqual(settings.SECRET_KEY, "")
