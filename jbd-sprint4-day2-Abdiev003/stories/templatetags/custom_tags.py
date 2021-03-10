from django.template import Library
from stories.models import Category

register = Library()


@register.simple_tag
def get_categories(ispublished=True):
    return Category.objects.filter(is_published=ispublished)
