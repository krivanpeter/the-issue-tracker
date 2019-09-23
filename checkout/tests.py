from django.test import TestCase
from .forms import OrderForm


# Create your tests here.
class OrderFormTest(TestCase):

    def test_cant_submit_order(self):
        test_form = OrderForm({
            'content': 'test content',
            'full_name': 'Test Name',
            'phone_number': 'Test Name',
            'country': 'Test Name',
        })
        self.assertFalse(test_form.is_valid())

    def test_submit_order(self):
        test_form = OrderForm({
            'content': 'test content',
            'full_name': 'Test Name',
            'phone_number': 'Test Name',
            'country': 'Test Name',
            'postcode': 'Test Name',
            'town_or_city': 'Test Name',
            'street_address1': 'Test Name',
            'street_address2': 'Test Name',
            'country': 'Test Name',
        })
        self.assertTrue(test_form.is_valid())

