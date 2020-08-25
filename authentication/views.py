from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import RegistrationForm
from .forms import LoginForm
# Create your views here.

def login(reponse):
    if reponse.method == "GET":
        form = LoginForm()
        return render(reponse, 'login.html', { 'form': form })
    else:
        form = LoginForm(reponse.POST)
        try:
            user = User.objects.get(email= reponse.POST.get("email"), password = reponse.POST.get("password"))
            reponse.session['username'] = user.firstname + ' ' + user.lastname
            reponse.session['userid'] = user.id
            return redirect('/games/games_rating')
        except:
            return HttpResponse('<h1>Failed to Login</h1>')
        return HttpResponse('<h1>Failed to Login</h1>')

def register(response):
    if response.method == "GET":
        form = RegistrationForm()
        return render(response, 'register.html', { 'form': form })
    else:
        form = RegistrationForm(response.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse('<h1>Registered...</h1> <a href="login">click here to login</a>')
            except:
                return HttpResponse('<h1>Failed to Register..! e-mail might already exists</h1>')
        return HttpResponse('<h1>Failed to Register..! e-mail might already exists</h1>')
        
