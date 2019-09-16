from django.contrib.auth.models import User
from django.test import TestCase


class TestViews(TestCase):
    def test_view_cart(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
