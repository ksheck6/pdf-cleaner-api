"""
Tests for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests for custom user model."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@exemple.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_emails = [
            ['test1@EXEMPLE.com', 'test1@exemple.com'],
            ['Test2@Exemple.com', 'Test2@exemple.com'],
            ['TEST3@EXEMPLE.COM', 'TEST3@exemple.com'],
            ['test4@exemple.COM', 'test4@exemple.com'],
        ]
        for email, execpected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, execpected)

    def test_new_user_without_email_raises_error(self):
        """ Test creating user without email raises ValueError """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
