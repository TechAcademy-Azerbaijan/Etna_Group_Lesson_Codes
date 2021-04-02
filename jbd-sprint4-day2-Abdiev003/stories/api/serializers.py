from rest_framework import serializers
from django.contrib.auth import  get_user_model

from accounts.serializers import UserSerializer
from stories.models import Recipe, Tag




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'title'
        ]


class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    author = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'slug',
            'order',
            'short_description',
            'image',
            'description',
            'created_at',
            'category',
            'author',
            'tags',
        ]


class RecipeCreateSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'order',
            'slug',
            'short_description',
            'image',
            'description',
            'created_at',
            'category',
            'author',
            'tags',
        ]
