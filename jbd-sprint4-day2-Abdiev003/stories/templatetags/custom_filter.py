from django.template import Library

register = Library()

# my_str = 'salam'
# my_str.split('a') # [s,l,m]


@register.filter
def my_split(my_str, value):
    return my_str.split(value)

