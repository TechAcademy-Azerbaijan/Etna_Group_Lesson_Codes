from django.urls import path
from stories.api.views import RecipeAPIView, RecipeDetailAPIView


urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(), name='recipes_api'),
    path('recipes/<int:pk>/', RecipeDetailAPIView.as_view(), name='recipes_detail_api')
]