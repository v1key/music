from django import forms

from .models import *
#from django.core.exceptions import ValidationError

#class SongForm(forms.Form):
#    song_title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#    song_time  = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
#    artist_title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#    album_title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#    genre_title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#    def save(self):
#        new_song = Song.objects.create(
#            song_title = self.cleaned_data['song_title'],
#            song_time = self.cleaned_data['song_time']
#        )
#        new_artist = Artist.objects.create(artist_title = self.cleaned_data['artist_title'])
#        new_album = Album.objects.create(album_title = self.cleaned_data['album_title'])
#        new_genre = Genre.objects.create(genre_title = self.cleaned_data['genre_title'])
#        return new_song, new_artist, new_album, new_genre
    #artist = self.cleaned_data['song_']
    #color = forms.ModelChoiceField(queryset=Color.objects.all())
    #speed = forms.ModelChoiceField(queryset=Speed.objects.all())

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = {'author_title', 'author_bio'}
        labels = {'author_title': 'Автор', 'author_bio': 'Биография'}

        widgets = {
            'author_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author_bio': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SongAuthorsForm(forms.ModelForm):
    class Meta:
        model = SongAuthors
        fields = {'author', 'song'}
        label = {'author': 'Автор', 'song': 'Трек'}

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'song': forms.Select(attrs={'class': 'form-control'}),
        }


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ('song_id',)
        labels = {'song_title': 'Трек', 'song_time': 'Время', 'artist': 'Исполнитель', 'album': 'Альбом', 'genre': 'Жанр'}

        widgets = {
            'song_title': forms.TextInput(attrs={'input type': 'text', 'class': 'form-control'}),
            'song_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'ЧЧ:ММ:СС', 'id': 'durationForm', 'maxlength': '8'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
        }

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('artist_title', 'artist_bio')
        labels = {'artist_title': 'Исполнитель', 'artist_bio': 'Биография'}

        widgets = {
            'artist_title': forms.TextInput(attrs={'class': 'form-control'}),
            'artist_bio': forms.Textarea(attrs={'class': 'form-control'})
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('genre_title', 'genre_description')
        labels = {'genre_title': 'Жанр', 'genre_description': 'Описание'}

        widgets = {
            'genre_title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre_description': forms.Textarea(attrs={'class': 'form-control'})
        }

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('label_title', 'label_description')
        labels = {'label_title': 'Лейбл', 'label_description': 'Описание'}

        widgets = {
            'label_title': forms.TextInput(attrs={'class': 'form-control'}),
            'label_description': forms.Textarea(attrs={'class': 'form-control'})
        }


class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ('producer_title', 'producer_bio')
        labels = {'producer_title': 'Продюсер', 'producer_bio': 'Биография'}

        widgets = {
            'producer_title': forms.TextInput(attrs={'class': 'form-control'}),
            'producer_bio': forms.Textarea(attrs={'class': 'form-control'})
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = {'album_title', 'album_type', 'date', 'producer', 'label', 'country'}
        labels = {'album_title': 'Альбом', 'album_type': 'Тип', 'date': 'Дата', 'producer': 'Продюсер', 'label': 'Лейбл', 'country': 'Страна'}

        widgets = {
            'album_title': forms.TextInput(attrs={'class': 'form-control'}),
            'album_type': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'ГГГГ:ММ:ДД', 'type': 'date'}),
            'producer': forms.Select(attrs={'class': 'form-control'}),
            'label': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
        }


class AlbumSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = {'song_id', 'album',}
        labels = {'album': 'Альбом'}

        widgets = {
            'song_id': forms.Select(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-control'}),
        }