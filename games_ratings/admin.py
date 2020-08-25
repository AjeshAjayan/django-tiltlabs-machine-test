from django.contrib import admin
from .models import Games

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(Games, GameAdmin)
