from django.test import TestCase
from .models import Enter


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about_page(self):
        response = self.client.get('/about', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_competition_page(self):
        response = self.client.get('/competition', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'competition.html')

    def test_get_login_page(self):
        response = self.client.get('/accounts/login', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
