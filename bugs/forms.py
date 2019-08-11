from django import forms
from .models import Bug, BugImages
import re


class BugReportForm(forms.ModelForm):
    # Bug Report Form
    title = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control bug-input',
            'placeholder': 'Give it a title...',
            'rows': '1'}),
        label='Title')
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control bug-input',
            'placeholder': 'Describe the issue here...',
            'rows': '3'}),
        label='Description')

    class Meta:
        model = Bug
        fields = (
            'title',
            'content',
        )

    def clean_title(self):
        title = re.sub(' +', ' ', self.cleaned_data.get('title').strip())
        return title

    def clean_content(self):
        content = re.sub(' +', ' ', self.cleaned_data.get('content').strip())
        return content


class BugImageForm(forms.ModelForm):
    images = forms.ImageField(
        required=False,
        label='',
        widget=forms.FileInput(
            attrs={
                'name': 'images',
                'multiple': True,
            })
    )

    class Meta:
        model = BugImages
        fields = ('images', )
