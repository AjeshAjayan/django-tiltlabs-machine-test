from django.urls import path
from .views import GamesView

urlpatterns = [
    path('games_rating', GamesView.as_view())
]