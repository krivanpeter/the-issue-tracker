from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    ReadOnlyPasswordHashField,
    PasswordChangeForm)
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from accounts.models import UserProfile
import re


# User Login Form
class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, label='Email',
        widget=forms.TextInput(
            attrs={'id': 'id_registration_email', 'type': 'email'}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput,
        required=True)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': "<span class='username_helper'>30 characters or fewer."
                        "Letters, digits and @/./+/-/_ only</span>",
        }

    def clean_email(self):
        email = re.sub(' +', ' ', self.cleaned_data.get('email'))
        username = re.sub(' +', ' ', self.cleaned_data.get('username'))
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = re.sub(' +', ' ', self.cleaned_data.get('password1'))
        password2 = re.sub(' +', ' ', self.cleaned_data.get('password2'))
        if not password1 or not password2:
            raise ValidationError("Password must not be empty")
        if password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2


# User Profile EditForm
class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bug-input',
            'rows': '1'}),
        label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bug-input',
            'rows': '1'}),
        label='Last Name')
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control bug-input',
            'rows': '1'}),
        label='E-mail')
    password = ReadOnlyPasswordHashField(
        label='Password',
        help_text=('Raw passwords are not stored, so there is no way to see '
                   'the password, but you can change it '
                   'using <a href=\"/profile/change-password/\">this form</a>.'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control bug-input',
            }),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

    def clean_first_name(self):
        first_name = re.sub(' +', ' ', self.cleaned_data.get('first_name').strip())
        return first_name

    def clean_last_name(self):
        last_name = re.sub(' +', ' ', self.cleaned_data.get('last_name').strip())
        return last_name

    def clean_email(self):
        email = re.sub(' +', ' ', self.cleaned_data.get('email').strip())
        return email

    def clean_password(self):
        # Necessary for tests to run without problem
        return ""


class EditUserForm(forms.ModelForm):
    avatar = forms.ImageField(
        required=False,
        label='Avatar',
        widget=forms.FileInput(
            attrs={
                'name': 'images'
            })
    )
    country = CountryField(blank=True).formfield(
        required=False,
        label='Country',
        widget=CountrySelectWidget(
            attrs={
                'class': 'form-control lazyselect',
            })
        )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bug-input',
                'rows': '1'}),
        label='Phone Number')
    postcode = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bug-input',
                'rows': '1'}),
        label='Postcode')
    town_or_city = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bug-input',
                'rows': '1'}),
        label='Town or City')
    street_address1 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bug-input',
                'rows': '1'}),
        label='Street Address')
    street_address2 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bug-input',
                'rows': '1'}),
        label='Street Address 2')
    county = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bug-input',
                'rows': '1'}),
        label='County')

    class Meta:
        model = UserProfile
        fields = (
            'avatar', 'country',
            'county', 'town_or_city',
            'postcode', 'street_address1',
            'street_address2', 'phone_number'
        )


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control bug-input'
