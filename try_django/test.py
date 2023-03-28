from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.test import TestCase
from articles.models import Article
import os


class TryDjangoProjectTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get("SECRET_KEY")
        # secret_key = settings.SECRET_KEY
        try:
            secure_password = validate_password(SECRET_KEY)
        except Exception as e:
            message = f"Error message: {e}"
            self.fail(message)
            # print(message)
        

