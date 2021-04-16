from django.test import TestCase
from django.conf import settings
from django.urls import reverse_lazy

from stories.models import Contact
from stories.views import ContactView


class TestContactView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.contact_url = f'/{settings.LANGUAGE_CODE}/contact/'
        cls.url = reverse_lazy('stories:contact')
        cls.view = ContactView()
        cls.valid_data = {
            'full_name': 'Idris Shabanli',
            'email': 'idris@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

        cls.invalid_data = {
            'full_name': 'Idris Shabanli',
            'email': 'idris',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

    def test_reverse_lazy_method(self):
        self.assertEqual(self.contact_url, self.url)

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_request(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        contact_data = Contact.objects.last()
        self.assertEqual(self.valid_data['full_name'], contact_data.full_name)
        self.assertEqual(self.valid_data['email'], contact_data.email)
        self.assertEqual(self.valid_data['message'], contact_data.message)
        self.assertRedirects(response, f'/{settings.LANGUAGE_CODE}/')

    def test_post_invalid_request(self):
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Keçərli e-poçt ünvanı daxil edin.", html=True)


    @classmethod
    def tearDownClass(cls):
        pass
