from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import UserProfile
from .models import Feature


class TestViews(TestCase):
    def test_cant_get_features_page_without_login(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 302)
        page = self.client.get("/features/", follow=True)
        self.assertTemplateUsed(page, "index.html")
        self.assertEqual(page.status_code, 200)

    def test_get_features_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")

    def test_get_feature_detail_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.new = Feature.objects.create(
            title="test-feature",
            slug="test-feature"
            )
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/features/test-feature/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featuredetail.html")

    def test_report_feature_no_upvotes_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/report-feature/")
        self.assertEqual(page.status_code, 302)

    def test_report_feature_enough_upvotes_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.userprofile = UserProfile.objects.get(user=self.user)
        self.userprofile.available_upvotes = 50
        self.userprofile.save()
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/report-feature/")
        self.assertEqual(page.status_code, 200)

    def test_upvote_feature_without_upvotes(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.bug = Feature.objects.create(
            title="test-feature",
            slug="test-feature"
        )
        response = self.client.get('/features/test-feature/upvote',  {'quantity': 5})
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'user_has_upvotes': False, 'max_reached': False, 'quantity': 5}
        )

    def test_upvote_feature_closed(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.userprofile = UserProfile.objects.get(user=self.user)
        self.userprofile.available_upvotes = 50
        self.userprofile.save()
        self.client.login(username='testuser', password='12345')
        self.bug = Feature.objects.create(
            title="test-feature",
            slug="test-feature",
            upvotes=50
        )
        response = self.client.get('/features/test-feature/upvote',  {'quantity': 5})
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'user_has_upvotes': True, 'max_reached': True, 'quantity': 0}
        )

    def test_upvote_feature_close_to_closing(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.userprofile = UserProfile.objects.get(user=self.user)
        self.userprofile.available_upvotes = 50
        self.userprofile.save()
        self.client.login(username='testuser', password='12345')
        self.bug = Feature.objects.create(
            title="test-feature",
            slug="test-feature",
            upvotes=40
        )
        response = self.client.get('/features/test-feature/upvote',  {'quantity': 5})
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'user_has_upvotes': True, 'max_reached': False, 'quantity': 5}
        )

    def test_upvote_feature_more_upvotes_then_needed(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.userprofile = UserProfile.objects.get(user=self.user)
        self.userprofile.available_upvotes = 50
        self.userprofile.save()
        self.client.login(username='testuser', password='12345')
        self.bug = Feature.objects.create(
            title="test-feature",
            slug="test-feature",
            upvotes=49
        )
        response = self.client.get('/features/test-feature/upvote',  {'quantity': 10})
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'user_has_upvotes': True, 'max_reached': True, 'quantity': 1}
        )
