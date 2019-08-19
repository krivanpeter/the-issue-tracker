from django.test import TestCase
from .forms import BugReportForm, BugImageForm


# Create your tests here.
class BugReportTests(TestCase):

    def test_cant_submit_bug_report(self):
        test_form = BugReportForm({'content': 'test content'})
        self.assertFalse(test_form.is_valid())

    def test_bug_report(self):
        test_form = BugReportForm({'title': 'test title', 'content': 'test content'})
        self.assertTrue(test_form.is_valid())


class BugImageTests(TestCase):

    def test_bug_no_image(self):
        test_form = BugImageForm({'images': ''})
        self.assertTrue(test_form.is_valid())

    def test_bug_image(self):
        test_form = BugImageForm({'images': '1.png'})
        self.assertTrue(test_form.is_valid())

    def test_bug_images(self):
        test_form = BugImageForm({'images': {'1.png', '2.png', '3.png'}})
        self.assertTrue(test_form.is_valid())
