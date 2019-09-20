from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory
from .views import delete_avatar


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_cant_get_profile_page_without_login(self):
        page = self.client.get("/profile/testuser")
        self.assertEqual(page.status_code, 301)
        page = self.client.get("/profile/testuser", follow=True)
        self.assertTemplateUsed(page, "index.html")
        self.assertEqual(page.status_code, 200)

    def test_get_profile_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/profile/testuser", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    def test_get_other_user_profile_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.otheruser = User.objects.create_user(username='otheruser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/profile/otheruser", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    def test_edit_profile(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        page = self.client.get("/profile/edit", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "editprofile.html")

    def test_delete_avatar(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.userprofile.avatar = "../media/profile_images/test.png"
        self.client.login(username='testuser', password='12345')
        self.factory = RequestFactory()
        request = self.factory.get('/accounts/delete-avatar/')
        request.user = self.user
        delete_avatar(request)
        self.assertEqual(self.user.userprofile.avatar, "../media/profile_images/male_def.png")

    def test_check_username_not_exists(self):
        response = self.client.get('/accounts/check_username/', {'username': 'testuser'})
        self.assertJSONEqual(response.content, {"username_is_taken": False})

    def test_check_username_exists(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        response = self.client.get('/accounts/check_username/', {'username': 'testuser'})
        self.assertJSONEqual(response.content, {"username_is_taken": True})

    def test_check_email_not_exists(self):
        response = self.client.get('/accounts/check_email/', {'email': 'testuser@testuser.com'})
        self.assertJSONEqual(response.content, {"email_is_taken": False})

    def test_check_email_exists(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        response = self.client.get('/accounts/check_email/', {'email': 'testuser@testuser.com'})
        self.assertJSONEqual(response.content, {"email_is_taken": True})

    def test_check_user_data_not_exists(self):
        response = self.client.post('/accounts/check_userdata/', {'username_or_email': 'testuser@testuser.com', 'password': '12345'})
        self.assertJSONEqual(response.content, {"username_or_password_error": True})

    def test_check_user_data_exists(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        response = self.client.post('/accounts/check_userdata/', {'username_or_email': 'testuser@testuser.com', 'password': '12345'})
        self.assertJSONEqual(response.content, {"username_or_password_error": False})

    def test_check_user_data_exists_incorrect_data(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@testuser.com', password='12345')
        response = self.client.post('/accounts/check_userdata/', {'username_or_email': 'usertest', 'password': '54321'})
        self.assertJSONEqual(response.content, {"username_or_password_error": True})
