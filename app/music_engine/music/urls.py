from django.urls import path

from .views import *

urlpatterns = [
    path('', music_library, name='music_library_url'),
]
