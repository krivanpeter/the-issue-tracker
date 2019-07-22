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

    def title(self):
        title = self.cleaned_data.get('title')
        return title

    def content(self):
        content = self.cleaned_data.get('content')
        return content
