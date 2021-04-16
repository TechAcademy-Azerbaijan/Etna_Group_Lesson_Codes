from django.test import TestCase

from stories.models import Contact


class TestContactModel(TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'full_name': 'Idris Shabanli',
            'email': 'idris@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }
        data2 = {
            'full_name': 'Yusif Huseynli',
            'email': 'yusif@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Ana sehifeden login sehifesine daxil ola bilmirem'
        }
        cls.contact_info1 = Contact.objects.create(**data)
        cls.contact_info2 = Contact.objects.create(**data2)

    def test_created_data(self):
        self.assertEqual(self.contact_info1.full_name, 'Idris Shabanli')
        self.assertEqual(self.contact_info2.full_name, 'Yusif Huseynli')

    def test_str_method(self):
        self.assertEqual(str(self.contact_info1), self.contact_info1.email)
        self.assertEqual(str(self.contact_info2), self.contact_info2.email)

    @classmethod
    def tearDownClass(cls):
        pass

