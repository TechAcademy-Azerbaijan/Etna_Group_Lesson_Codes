from rest_framework import serializers
from django.contrib.auth import  get_user_model
from stories.models import Recipe, Tag

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'image',
            'username',
            'email',
            'bio',
            'gender'
        ]


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