from django.shortcuts import render

def music_library(request):
    return render(request, 'music/base.html')
