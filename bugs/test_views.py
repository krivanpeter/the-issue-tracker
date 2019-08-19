from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bug


class TestViews(TestCase):
    def test_cant_get_bugs_page_without_login(self):
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 302)
        page = self.client.get("/bugs/", follow=True)
        self.assertTemplateUsed(page, "index.html")
        self.assertEqual(page.status_code, 200)

    def test_get_bugs_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")

    def test_get_bug_detail_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.new = Bug.objects.create(
            title="test-bug",
            slug="test-bug"
            )
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/bugs/test-bug/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugdetail.html")

    def test_report_bug_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/report-bug/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "reportbug.html")
