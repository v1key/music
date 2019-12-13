from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_music(request):
    return redirect('music_library_url', permanent=True)
