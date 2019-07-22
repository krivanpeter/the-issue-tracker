from django import forms
from .models import Bug, BugImages


class BugReportForm(forms.ModelForm):
    # Bug Report Form
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control bug-input',
            'placeholder': 'Describe the issue...',
            'rows': '3'}),
        label='The issue')

    class Meta:
        model = Bug
        fields = (
            'title',
            'content',
        )

    def title(self):
        title = self.cleaned_data.get('title')
        return title

    def content(self):
        content = self.cleaned_data.get('content')
        return content

class BugImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = BugImages
        fields = (
            'image',
        )