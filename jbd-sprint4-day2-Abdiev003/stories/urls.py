from django.urls import path

from .views import (
    HomePage, AboutPage, StoriesPage, ContactPage, like_recipe, liked_recipe_page,
    RecipeListView,
    RecipeDetailView,
    # RecipesPage,
)

app_name = "stories"

urlpatterns = [
    path('', HomePage, name="index"),
    path('about/', AboutPage, name="about"),
    path('stories/', StoriesPage, name="stories"),
    path('recipes/', RecipeListView.as_view(), name="recipes"),
    path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('contact/', ContactPage, name="contact"),
    path('like/', like_recipe, name='like'),
    path('liked_recipe_page/', liked_recipe_page, name='liked_recipe_page')
]
