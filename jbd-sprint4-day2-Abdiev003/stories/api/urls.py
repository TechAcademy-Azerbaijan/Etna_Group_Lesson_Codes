from django.urls import path
from stories.api.views import recipes


urlpatterns = [
    path('recipes/', recipes, name='recipes_api')
]