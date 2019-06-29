from django import forms
from bugs.models import Bug


# Bug Report Form
class BugReportForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = (
            'title',
            'content',
        )