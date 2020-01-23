from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import redirect_music

from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('', redirect_music)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
