import json

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from stories.models import Recipe, Subscriber
from stories.api.serializers import RecipeSerializer, RecipeCreateSerializer, SubscriberSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView


class RecipeAPIView(ListCreateAPIView):
    queryset = Recipe.objects.filter(is_published=True)
    serializer_class = RecipeSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return RecipeCreateSerializer


class RecipeDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Recipe.objects.filter(is_published=True)
    serializer_class = RecipeSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return RecipeCreateSerializer


class SubscribeAPIView(CreateAPIView):
    queryset = Subscriber.objects.filter(is_active=True)
    serializer_class = SubscriberSerializer


#
# @api_view(('GET', 'POST'))
# def recipes(request):
#     if request.method == 'POST':
#         recipe_data = request.data
#         serializer = RecipeCreateSerializer(data=recipe_data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     recipes = Recipe.objects.filter(is_published=True)
#     serializer = RecipeSerializer(recipes, many=True, context={'request': request})
#     return Response(serializer.data)


# class RecipeAPIView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         recipes = Recipe.objects.filter(is_published=True)
#         filter_by = json.loads(json.dumps(request.GET))
#         if filter_by:
#             recipes = recipes.filter(**filter_by)  # title=resept
#         serializer = RecipeSerializer(recipes, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         recipe_data = request.data
#         serializer = RecipeCreateSerializer(data=recipe_data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class RecipeDetailAPIView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         recipe_id = kwargs.get('pk')
#         recipe = Recipe.objects.filter(pk=recipe_id, is_published=True).first()
#         if not recipe:
#             raise NotFound
#         serializer = RecipeSerializer(recipe, context={'request': request})
#         return Response(serializer.data)
#
#     def put(self, request, *args, **kwargs):
#         recipe_data = request.data
#         recipe_id = kwargs.get('pk')
#         recipe = Recipe.objects.filter(pk=recipe_id, is_published=True).first()
#         if not recipe:
#             raise NotFound
#         serializer = RecipeCreateSerializer(data=recipe_data, instance=recipe, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, request, *args, **kwargs):
#         recipe_data = request.data
#         recipe_id = kwargs.get('pk')
#         recipe = Recipe.objects.filter(pk=recipe_id, is_published=True).first()
#         if not recipe:
#             raise NotFound
#         serializer = RecipeCreateSerializer(data=recipe_data, instance=recipe,
#                                             partial=True, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, *args, **kwargs):
#         recipe_id = kwargs.get('pk')
#         recipe = Recipe.objects.filter(pk=recipe_id, is_published=True)
#         if not recipe:
#             raise NotFound
#         recipe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
