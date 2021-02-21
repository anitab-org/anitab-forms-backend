import unittest

from django.test import TestCase

from main import settings


class TestConfig(TestCase):
    def test_app_testing_config(self):
        self.assertIsNotNone(settings.SECRET_KEY)
        self.assertNotEqual(settings.SECRET_KEY, "")


if __name__ == "__main__":
    unittest.main()
