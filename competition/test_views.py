from django.test import TestCase
from .models import Enter


# Test taken from "Hello Django"
class TestViews(TestCase):
    """
    Tests for views.
    """
    def test_get_home_page(self):
        """
        Verify home page loads
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_rules_page(self):
        """
        Verify rules page loads
        """
        response = self.client.get('/rules', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rules.html')

    def test_get_competition_page(self):
        """
        Verify competition page loads
        """
        response = self.client.get('/competition', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'competition.html')

    def test_get_login_page(self):
        """
        Verify login page loads
        """
        response = self.client.get('/accounts/login', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
