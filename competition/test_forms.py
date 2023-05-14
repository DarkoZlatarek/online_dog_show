from django.test import TestCase
from .forms import EnterForm, CommentForm


class TestEnterForm(TestCase):

    def test_title_is_required(self):
        form = EnterForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_content_is_required(self):
        form = EnterForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_featured_image_is_required(self):
        form = EnterForm({'featured_image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('featured_image', form.errors.keys())
        self.assertEqual(
            form.errors['featured_image'][0], 'No file selected!')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = EnterForm()
        self.assertEqual(
            form.Meta.fields, ('title', 'content', 'featured_image'))


class TestCommentForm(TestCase):

    def test_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
