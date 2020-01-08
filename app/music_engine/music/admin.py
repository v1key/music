from django.contrib import admin

from .models import *

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_id', 'song_title', 'song_time', 'artist', 'album', 'genre')
