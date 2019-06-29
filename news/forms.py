from django import forms
from .models import New


# User Login Form
class CreateNewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = (
            'title',
            'content',
            'image'
        )