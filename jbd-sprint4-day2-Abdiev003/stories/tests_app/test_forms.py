from django.test import TestCase

from stories.forms import ContactForm


class TestContactForm(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_data = {
            'full_name': 'Idris Shabanli',
            'email': 'idris@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }

        cls.invalid_data = {
            'email': 'idris@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }
        cls.form = ContactForm

    def test_form_with_valid_data(self):
        form = self.form(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = self.form(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)
        self.assertIn('Bu sahə tələb edilir.', form.errors['full_name'])

    @classmethod
    def tearDownClass(cls):
        pass