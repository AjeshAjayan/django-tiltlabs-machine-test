from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Games, GamesRatings
from authentication.models import User

# Create your views here.

class GamesView(generic.ListView):
    template_name = 'games.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Games.objects.raw('SELECT * FROM game_rating.games_ratings_games g left join games_ratings_gamesratings gr on  gr.game_id_id = g.id and gr.user_id_id = ' + str(self.request.session['userid']))

    def post(self, request, *args, **kwargs):
        ratigs = self.request.POST
        games = Games.objects.all()
        is_saved = False
        for game in games:
            if (ratigs.get(str(game.id)) is not None) and (ratigs.get(str(game.id)) is not ''):
                is_saved = True
                user = User.objects.get(pk= self.request.session['userid'])
                gamesRatings = GamesRatings(game_id= game, user_id= user, rating= int(ratigs.get(str(game.id))))
                gamesRatings.save()
        if is_saved:
            return HttpResponse('<h1>Saved</h1>')
        else:
            return HttpResponse('<h1>Nothing to save</h1>')


