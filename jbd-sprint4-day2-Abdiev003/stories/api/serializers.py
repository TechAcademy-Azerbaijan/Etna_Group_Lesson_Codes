from rest_framework import serializers
from django.contrib.auth import  get_user_model

from accounts.serializers import UserSerializer
from stories.models import Recipe, Tag, Subscriber, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'title'
        ]


class CommentSerializer(serializers.ModelSerializer):
    sub_comments = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = (
            'id',
            'recipe',
            'author',
            'content',
            'sub_comments'
        )

    def get_sub_comments(self, parent_comment):
        sub_comments = parent_comment.sub_comments.all()
        return CommentSerializer(sub_comments, many=True).data


class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    author = UserSerializer()
    tags = TagSerializer(many=True)
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

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
            'comments',
            'comment_count',
        ]

    def get_comments(self, recipe):
        return CommentSerializer(recipe.comment.filter(parent_comment__isnull=True), many=True).data

    def get_comment_count(self, recipe):
        return recipe.comment.count()


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


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = [
            'id',
            'email',
            'created_at',
            'updated_at',
        ]