from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email successful"""
        email = 'test_email@example.com'
        password = 'test_password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test_email@EXAMPLE.com'
        user = get_user_model().objects.create_user(
            email=email, password='test_password'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user with no raises email error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None, password='test_password'
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email="test_super_email@example.com", password="test_password"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
