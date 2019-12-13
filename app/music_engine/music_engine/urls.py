from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import redirect_music

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('', redirect_music)
]
