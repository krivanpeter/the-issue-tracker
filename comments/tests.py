from django.test import TestCase
from .forms import CommentForm


# Create your tests here.
class OrderFormTest(TestCase):

    def test_cant_send_comment(self):
        test_form = CommentForm({
            'content': '',
        })
        self.assertFalse(test_form.is_valid())

    def test_send_comment(self):
        test_form = CommentForm({
            'content': 'Test comment',
        })
        self.assertFalse(test_form.is_valid())