import unittest
import os
from django.test import TestCase
from main import settings

class TestConfig(TestCase):
    def test_app_testing_config(self):
        print(os.environ['SECRET_KEY'])
        self.assertIsNotNone(settings.SECRET_KEY)
        self.assertNotEqual(settings.SECRET_KEY,'')
 
if __name__ == "__main__":
    unittest.main()
