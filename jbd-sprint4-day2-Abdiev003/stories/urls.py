from django.urls import path

from .views import HomePage, AboutPage, StoriesPage, RecipesPage, ContactPage

app_name = "stories"

urlpatterns = [
    path('', HomePage, name="index"),
    path('about/', AboutPage, name="about"),
    path('stories/', StoriesPage, name="stories"),
    path('recipes/', RecipesPage, name="recipes"),
    path('contact/', ContactPage, name="contact"),
]
