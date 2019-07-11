from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from accounts.models import UserProfile


# User Login Form
class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


# User Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(
        attrs={'id': 'id_registration_email', 'type': 'email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput, required=True)
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': "<span class='username_helper'>30 characters or fewer. Letters, digits and @/./+/-/_ only</span>",
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 or not password2:
            raise ValidationError("Password must not be empty")
        if password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2


# User Profile EditForm
class EditProfileForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                     "the password, but you can change it "
                                                     "using <a href=\"/profile/change-password/\">this form</a>."))
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'avatar',
            'gender'
        )