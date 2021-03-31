from django.core.management.base import BaseCommand
from stories.models import Recipe


class Command(BaseCommand):
    help = 'Translate Recipe Data'

    # def add_arguments(self, parser):
    #     parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        recipes = Recipe.objects.all()
        for recipe in recipes:
            recipe.title_az = recipe.title
            recipe.title_en = recipe.title
            recipe.title_ru = recipe.title
            recipe.slug_az = recipe.slug
            recipe.slug_en = recipe.slug
            recipe.slug_ru = recipe.slug
            recipe.short_description_az = recipe.short_description
            recipe.short_description_en = recipe.short_description
            recipe.short_description_ru = recipe.short_description
            recipe.description_az = recipe.description
            recipe.description_en = recipe.description
            recipe.description_ru = recipe.description
            recipe.save()
