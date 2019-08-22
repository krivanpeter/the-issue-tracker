from django import forms
from .models import Feature
import re


class FeatureReportForm(forms.ModelForm):
    # Feature Report Form
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
        model = Feature
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
