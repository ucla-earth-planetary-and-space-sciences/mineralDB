from collection import views
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse


class CollectionPageTests(TestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/collection/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('collection'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('collection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection_list.html')

    def test_detail_view_uses_correct_template(self):
        response = self.client.get(reverse('collection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collection_list.html')

#
# def test_about_page_contains_correct_html(self):
#     response = self.client.get('/about/')
#     self.assertContains(response, '<h1>About page</h1>')
#
#
# def test_about_page_does_not_contain_incorrect_html(self):
#     response = self.client.get('/')
#     self.assertNotContains(
#         response, 'Hi there! I should not be on the page.')
