from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    def test_cant_get_news_page_without_login(self):
        page = self.client.get("/news/")
        self.assertEqual(page.status_code, 302)
        page = self.client.get("/news/", follow=True)
        self.assertTemplateUsed(page, "index.html")
        self.assertEqual(page.status_code, 200)

    def test_get_news_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/news/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "news.html")
