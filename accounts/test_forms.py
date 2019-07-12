from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm, EditProfileForm, EditUserForm


# Create your tests here.
class UserLoginTests(TestCase):

    def test_can_login_with_just_a_name(self):
        form = UserLoginForm({'username': 'Create Tests'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_names(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])