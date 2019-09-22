from django.contrib.auth.models import User
from django.test import TestCase


class TestViews(TestCase):
    def test_cant_get_packages_page(self):
        page = self.client.get("/packages/")
        self.assertEqual(page.status_code, 302)
        page = self.client.get("/packages", follow=True)
        self.assertTemplateUsed(page, "index.html")
        self.assertEqual(page.status_code, 200)

    def test_get_packages_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/packages/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "packages.html")
