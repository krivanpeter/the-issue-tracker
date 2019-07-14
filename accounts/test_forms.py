from django.contrib.auth.models import User
from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


# Create your tests here.
class UserLoginTests(TestCase):

    def test_login(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        test_form = UserLoginForm({'username_or_email': 'testuser', 'password': '12345'})
        self.assertTrue(test_form.is_valid())

    def test_cant_login_with_just_a_name(self):
        test_form = UserLoginForm({'username_or_email': 'testuser'})
        self.assertFalse(test_form.is_valid())

    def test_cant_login_with_just_a_password(self):
        test_form = UserLoginForm({'username_or_email': '', 'password': '12345'})
        self.assertFalse(test_form.is_valid())


class UserRegisterTests(TestCase):

    def test_register(self):
        test_form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'testuser@testuser.com',
                                     'password1': '12345',
                                     'password2': '12345'})
        self.assertTrue(test_form.is_valid())

    def test_cant_register_with_invalid_email(self):
        test_form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'testuser.com',
                                     'password1': '12345',
                                     'password2': '12345'})
        self.assertFalse(test_form.is_valid())

    def test_cant_register_with_not_matching_password(self):
        test_form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'testuser.com',
                                     'password1': '54321',
                                     'password2': '12345'})
        self.assertFalse(test_form.is_valid())

    def test_cant_register_with_existing_username(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        test_form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'testuser123@testuser.com',
                                     'password1': '12345',
                                     'password2': '12345'})
        self.assertFalse(test_form.is_valid())