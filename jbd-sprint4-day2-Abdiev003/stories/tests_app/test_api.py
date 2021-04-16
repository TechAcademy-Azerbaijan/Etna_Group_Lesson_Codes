from django.test import TestCase
from django.test.client import Client

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from rest_framework import status

from stories.api.serializers import RecipeSerializer

from stories.models import Recipe, Category

User = get_user_model()


class RecipeAPITest(TestCase):
    """ Test module for GET all recipes API """

    @classmethod
    def setUpClass(cls):
        category = Category.objects.create(title='Category', image='cate.png')
        author = User.objects.create_user(username='ali', email='ali@gmail.com', password='25qawszxxckjnwd')
        cls.valid_data = {
            'category': category,
            'author': author,
            'title': 'Title',
            'short_description': 'short_description',
            'description': 'skjdfnbsjkdfnsdjk',
            'image': 'recipe.png',
        }

        cls.recipe1 = Recipe.objects.create(**cls.valid_data)
        cls.client = Client

    def test_get_all_recipes(self):
        # get API response
        response = self.client.get(reverse_lazy('api:recipes_api'))
        # get data from db
        recipes = Recipe.objects.all()
        # print(self.client.request)
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @classmethod
    def tearDownClass(cls):
        pass