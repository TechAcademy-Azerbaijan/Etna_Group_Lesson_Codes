from django.urls import path

from .views import HomePage, AboutPage, StoriesPage, RecipesPage, ContactPage, like_recipe, liked_recipe_page

app_name = "stories"

urlpatterns = [
    path('', HomePage, name="index"),
    path('about/', AboutPage, name="about"),
    path('stories/', StoriesPage, name="stories"),
    path('recipes/', RecipesPage, name="recipes"),
    path('contact/', ContactPage, name="contact"),
    path('like/', like_recipe, name='like'),
    path('liked_recipe_page/', liked_recipe_page, name='liked_recipe_page')
]
