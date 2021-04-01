from rest_framework.response import Response
from rest_framework import status
from stories.models import Recipe
from stories.api.serializers import RecipeSerializer, RecipeCreateSerializer
from rest_framework.decorators import api_view


@api_view(('GET', 'POST'))
def recipes(request):
    if request.method == 'POST':
        recipe_data = request.data
        serializer = RecipeCreateSerializer(data=recipe_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    recipes = Recipe.objects.filter(is_published=True)
    serializer = RecipeSerializer(recipes, many=True, context={'request': request})

    # serialized_recipe_list = [recipe.serialized_data for recipe in recipes]
    # json_data = {
    #     'recipes': serialized_recipe_list
    # }
    return Response(serializer.data)
