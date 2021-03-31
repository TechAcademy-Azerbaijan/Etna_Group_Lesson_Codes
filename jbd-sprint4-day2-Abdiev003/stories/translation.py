from modeltranslation.translator import translator, TranslationOptions
from stories.models import (
    Recipe,
    Tag,
    Category
)


class TagTranslationOptions(TranslationOptions):
    fields = ('title', )


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'short_description', 'description')


translator.register(Recipe, RecipeTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
