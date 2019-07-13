from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm, EditUserForm, EditProfileForm


# Create your tests here.
class UserLoginTests(TestCase):

    def test_login(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        form = UserLoginForm({'username_or_email': 'testuser', 'password': '12345'})
        self.assertTrue(form.is_valid())

    def test_cant_login_with_just_a_name(self):
        form = UserLoginForm({'username_or_email': 'testuser'})
        self.assertFalse(form.is_valid())

    def test_cant_login_with_just_a_password(self):
        form = UserLoginForm({'username_or_email': '', 'password': '12345'})
        self.assertFalse(form.is_valid())


class UserRegisterTests(TestCase):

    def test_register(self):
        form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'testuser@testuser.com',
                                     'password1': '12345',
                                     'password2': '12345'})
        self.assertTrue(form.is_valid())

    def test_cant_register_with_invalid_email(self):
        form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'testuser.com',
                                     'password1': '12345',
                                     'password2': '12345'})
        self.assertFalse(form.is_valid())

    def test_cant_register_with_not_matching_password(self):
        form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'testuser.com',
                                     'password1': '54321',
                                     'password2': '12345'})
        self.assertFalse(form.is_valid())

    def test_cant_register_with_existing_username(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        form = UserRegistrationForm({'username': 'testuser',
                                     'email': 'testuser@testuser.com',
                                     'password1': '12345',
                                     'password2': '12345'})
        self.assertFalse(form.is_valid())


class EditProfileFormTests(TestCase):

    def test_edit_profile(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        form = EditProfileForm({'first_name': 'Test2',
                                'last_name': 'Test2',
                                'email': 'test@testuser.com',
                                'password': '12345'})
        self.assertTrue(form.is_valid())