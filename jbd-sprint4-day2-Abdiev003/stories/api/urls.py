from django.urls import path
from stories.api.views import RecipeAPIView, RecipeDetailAPIView, SubscribeAPIView

app_name = 'api'

urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(), name='recipes_api'),
    path('recipes/<int:pk>/', RecipeDetailAPIView.as_view(), name='recipes_detail_api'),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe')
]