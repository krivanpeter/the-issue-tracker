from django import forms
import re


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control comment-input',
            'placeholder': 'Write a comment...',
            'rows': '3'}),
        label='')

    def clean_content(self):
        content = re.sub(' +', ' ', self.cleaned_data.get('content').strip())
        return content
