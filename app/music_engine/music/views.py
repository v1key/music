from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.db.models import Q

from .forms import *
from .models import *

import pygal
from pygal.style import CleanStyle

def music_library(request):
    return render(request, 'music/base.html')

class SongsList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        sort = request.GET.getlist('sort')
        if search_query:
            songs = Song.objects.filter(Q(song_title__icontains=search_query) | Q(artist__artist_title__icontains=search_query) | Q(album__album_title__icontains=search_query) | Q(genre__genre_title__icontains=search_query) | Q(songauthors__author__author_title__icontains=search_query)).distinct()
        else:

            songs = Song.objects.all().order_by(*sort)

        authors = SongAuthors.objects.all().order_by('author__author_title')
        return render(request, 'music/songs_list.html', context = { 'songs': songs, 'authors': authors })

class SongsAuthorsAdd(View):
    def get(self, request):
        song_authors_form = SongAuthorsForm()
        return render(request, 'music/songs_authors_add.html', context={'song_authors_form': song_authors_form})

    def post(self, request):
        song_authors_form = SongAuthorsForm(request.POST)
        if song_authors_form.is_valid():
            new_song_author = song_authors_form.save()
        return render(request, 'music/songs_authors_add.html', context={'song_authors_form': song_authors_form})

class SongsCreate(View):
    def get(self, request):
        song_form = SongForm()
        author_form = AuthorForm()
        song_authors_form = SongAuthorsForm()
        context = {
            'song_form': song_form,
            'author_form': author_form,
            'song_authors_form': song_authors_form
        }
        return render(request, 'music/songs_create.html', context=context)

    def post(self, request):
        song_form = SongForm(request.POST)
        author_form = AuthorForm(request.POST)
        song_authors_form = SongAuthorsForm(request.POST)
        if song_form.is_valid():
            new_song = song_form.save()


        if song_authors_form.is_valid():
            new_song_author = song_authors_form.save()

        return redirect('songs_create_url')


class SongsUpdate(View):
    def get(self, request, song_id):
        song = Song.objects.get(song_id__iexact=song_id)
        bound_form = SongForm(instance=song)
        song_authors = SongAuthors.objects.all()
        
        return render(request, 'music/songs_update.html', context = { 'song_form': bound_form, 'song': song, 'authors': song_authors})

    def post(self, request, song_id):
        song = Song.objects.get(song_id__iexact=song_id)
        bound_form = SongForm(request.POST, instance=song)
        if bound_form.is_valid():
            new_song = bound_form.save()

        return redirect('songs_update_url', song_id)


class SongsDelete(View):
    def get(self, request, song_id):
        song = Song.objects.get(song_id__iexact=song_id)
        return render(request, 'music/songs_delete.html', context = { 'song': song })

    def post(self, request, song_id):
        song = Song.objects.get(song_id__iexact=song_id)
        song.delete()

        return redirect('songs_list_url')

class SongsAuthorsDelete(View):
    def get(self, request, id):
        song_authors = SongAuthors.objects.get(id__iexact=id)
        return render(request, 'music/songs_authors_delete.html', context = { 'author': song_authors })

    def post(self, request, id):
        song_author = SongAuthors.objects.get(id__iexact=id)
        song_author.delete()

        return redirect('songs_list_url')


class AuthorsList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        sort = request.GET.getlist('sort')
        if search_query:
            authors = Author.objects.filter(Q(author_title__icontains=search_query) | Q(author_bio__icontains=search_query))
        else:
            authors = Author.objects.all().order_by(*sort)
        return render(request, 'music/authors_list.html', context = { 'authors': authors })


class AuthorsCreate(View):
    def get(self, request):
        author_form = AuthorForm()
        context = {
            'author_form': author_form,
        }
        return render(request, 'music/authors_create.html', context=context)

    def post(self, request):
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            new_author = author_form.save()

        return redirect('authors_create_url')

class AuthorsDetail(View):
    def get(self, request, slug):
        author = Author.objects.get(slug__iexact=slug)
        return render(request, 'music/authors_detail.html', context = { 'author': author })


class AuthorsUpdate(View):
    def get(self, request, slug):
        author = Author.objects.get(slug__iexact=slug)
        bound_form = AuthorForm(instance=author)
        return render(request, 'music/authors_update.html', context = { 'author_form': bound_form, 'author': author })

    def post(self, request, slug):
        author = Author.objects.get(slug__iexact=slug)
        bound_form = AuthorForm(request.POST, instance=author)

        if bound_form.is_valid():
            new_author = bound_form.save()
        return redirect('authors_update_url', slug)


class AuthorsDelete(View):
    def get(self, request, slug):
        author = Author.objects.get(slug__iexact=slug)
        return render(request, 'music/authors_delete.html', context = { 'author': author })

    def post(self, request, slug):
        author = Author.objects.get(slug__iexact=slug)
        author.delete()

        return redirect('authors_list_url')

class AlbumsCreate(View):
    def get(self, request):
        album_form = AlbumForm()
        context = {
            'album_form': album_form,
        }
        return render(request, 'music/albums_create.html', context=context)

    def post(self, request):
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            new_album = album_form.save()
        #if album_form.is_valid():
         #   new_song = album_song_form.save()
        return redirect('albums_create_url')


class AlbumsUpdate(View):
    def get(self, request, slug):
        album = Album.objects.get(slug__iexact=slug)
        #song = Song.objects.get(album__iexact=album[0].album_title)
        bound_form = AlbumForm(instance=album)
        #bound_form_song = AlbumSongForm(instance=song)
        context = {
            'album_form': bound_form,
            'album': album
        }
        return render(request, 'music/albums_update.html', context=context)

    def post(self, request, slug):
        album = Album.objects.get(slug__iexact=slug)
       # song = Song.objects.get(album__iexact=album[0].album_title)
        bound_form = AlbumForm(request.POST, instance=album)
       # bound_form_song = AlbumSongForm(request.POST, instance=song)

        if bound_form.is_valid():
            new_album = bound_form.save()
        
       # if bound_form_song.is_valid():
        #    new_song = bound_form_song.save()

        return redirect('albums_update_url', slug)

class AlbumsDelete(View):
    def get(self, request, slug):
        album = Album.objects.get(slug__iexact=slug)
        return render(request, 'music/albums_delete.html', context = { 'album': album })

    def post(self, request, slug):
        album = Album.objects.get(slug__iexact=slug)
        album.delete()

        return redirect('albums_list_url')

class ArtistsCreate(View):
    def get(self, request):
        artist_form = ArtistForm()
        context = {
            'artist_form': artist_form,
        }
        return render(request, 'music/artists_create.html', context=context)

    def post(self, request):
        artist_form = ArtistForm(request.POST)
        if artist_form.is_valid():
            new_artist = artist_form.save()
        if artist_form.is_valid():
            new_artist = artist_form.save()
        return redirect('artists_create_url')

class ArtistsUpdate(View):
    def get(self, request, slug):
        artist = Artist.objects.get(slug__iexact=slug)
        bound_form = ArtistForm(instance=artist)
        return render(request, 'music/artists_update.html', context = { 'artist_form': bound_form, 'artist': artist })

    def post(self, request, slug):
        artist = Artist.objects.get(slug__iexact=slug)
        bound_form = ArtistForm(request.POST, instance=artist)

        if bound_form.is_valid():
            new_artist = bound_form.save()

        return redirect('artists_update_url', slug)

class ArtistsDelete(View):
    def get(self, request, slug):
        artist = Artist.objects.get(slug__iexact=slug)
        return render(request, 'music/artists_delete.html', context = { 'artist': artist })

    def post(self, request, slug):
        artist = Artist.objects.get(slug__iexact=slug)
        artist.delete()

        return redirect('artists_list_url')


class LabelsCreate(View):
    def get(self, request):
        label_form = LabelForm()
        context = {
            'label_form': label_form,
        }
        return render(request, 'music/labels_create.html', context=context)

    def post(self, request):
        label_form = LabelForm(request.POST)
        if label_form.is_valid():
            new_label = label_form.save()
        if label_form.is_valid():
            new_label = label_form.save()
        return redirect('labels_create_url')

class ProducersCreate(View):
    def get(self, request):
        producer_form = ProducerForm()
        context = {
            'producer_form': producer_form,
        }
        return render(request, 'music/producers_create.html', context=context)

    def post(self, request):
        producer_form = ProducerForm(request.POST)
        if producer_form.is_valid():
            new_producer = producer_form.save()
        if producer_form.is_valid():
            new_producer = producer_form.save()
        return redirect('producers_create_url')

class ProducersUpdate(View):
    def get(self, request, slug):
        producer = Producer.objects.get(slug__iexact=slug)
        bound_form = ProducerForm(instance=producer)
        return render(request, 'music/producers_update.html', context = { 'producer_form': bound_form, 'producer': producer })

    def post(self, request, slug):
        producer = Producer.objects.get(slug__iexact=slug)
        bound_form = ProducerForm(request.POST, instance=producer)

        if bound_form.is_valid():
            new_producer = bound_form.save()
        return redirect('producers_update_url', slug)


class ProducersDelete(View):
    def get(self, request, slug):
        producer = Producer.objects.get(slug__iexact=slug)
        return render(request, 'music/producers_delete.html', context = { 'producer': producer })

    def post(self, request, slug):
        producer = Producer.objects.get(slug__iexact=slug)
        producer.delete()

        return redirect('producers_list_url')


class AlbumsList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        sort = request.GET.getlist('sort')
        if search_query:
            albums = Album.objects.filter(Q(album_title__icontains=search_query) | Q(album_type__album_type_title__icontains=search_query) | Q(date__icontains=search_query) | Q(country__country_title__icontains=search_query) | Q(producer__producer_title__icontains=search_query) | Q(label__label_title__icontains=search_query))
        else:
            albums = Album.objects.all().order_by(*sort)
 
            
        songs = Song.objects.all()
        #songs = Song.objects.filter(artist_id__in=foo_queryset.values(albums))
        return render(request, 'music/albums_list.html', context = { 'albums': albums, 'songs': songs })


class AlbumsDetail(View):
    def get(self, request, slug):
        album = Album.objects.get(slug__iexact=slug)
        songs = Song.objects.all()
        return render(request, 'music/albums_detail.html', context = { 'album': album, 'songs': songs })

class ArtistsDetail(View):
    def get(self, request, slug):
        artist = Artist.objects.get(slug__iexact=slug)
        return render(request, 'music/artists_detail.html', context = { 'artist': artist })


class ArtistsList(View):
    def get(self, request):
        sort = request.GET.getlist('sort')
        search_query = request.GET.get('search', '')
        if search_query:
            artists = Artist.objects.filter(Q(artist_title__icontains=search_query) | Q(artist_bio__icontains=search_query) )
        else:
            artists = Artist.objects.all().order_by(*sort)
        return render(request, 'music/artists_list.html', context = { 'artists': artists })


class GenresList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        sort = request.GET.getlist('sort')
        if search_query:
            genres = Genre.objects.filter(Q(genre_title__icontains=search_query) | Q(genre_description__icontains=search_query))
        else:
            genres = Genre.objects.all().order_by(*sort)
        return render(request, 'music/genres_list.html', context = { 'genres': genres })


class GenresCreate(View):
    def get(self, request):
        genre_form = GenreForm()
        context = {
            'genre_form': genre_form,
        }
        return render(request, 'music/genres_create.html', context=context)

    def post(self, request):
        genre_form = GenreForm(request.POST)
        if genre_form.is_valid():
            new_genre = genre_form.save()
        if genre_form.is_valid():
            new_genre = genre_form.save()
        return redirect('genres_create_url')

class GenresDetail(View):
    def get(self, request, slug):
        genre = Genre.objects.get(slug__iexact=slug)
        return render(request, 'music/genres_detail.html', context = { 'genre': genre })


class GenresUpdate(View):
    def get(self, request, slug):
        genre = Genre.objects.get(slug__iexact=slug)
        bound_form = GenreForm(instance=genre)
        return render(request, 'music/genres_update.html', context = { 'genre_form': bound_form, 'genre': genre })

    def post(self, request, slug):
        genre = Genre.objects.get(slug__iexact=slug)
        bound_form = GenreForm(request.POST, instance=genre)

        if bound_form.is_valid():
            new_genre = bound_form.save()
        return redirect('genres_update_url', slug)


class GenresDelete(View):
    def get(self, request, slug):
        genre = Genre.objects.get(slug__iexact=slug)
        return render(request, 'music/genres_delete.html', context = { 'genre': genre })

    def post(self, request, slug):
        genre = Genre.objects.get(slug__iexact=slug)
        genre.delete()

        return redirect('genres_list_url')


class LabelsList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        sort = request.GET.getlist('sort')
        if search_query:
            labels = Label.objects.filter(Q(label_title__icontains=search_query) | Q(label_description__icontains=search_query))
        else:
            labels = Label.objects.all().order_by(*sort)
        return render(request, 'music/labels_list.html', context = { 'labels': labels })


class LabelsDetail(View):
    def get(self, request, slug):
        label = Label.objects.get(slug__iexact=slug)
        return render(request, 'music/labels_detail.html', context = { 'label': label })

class LabelsUpdate(View):
    def get(self, request, slug):
        label = Label.objects.get(slug__iexact=slug)
        bound_form = LabelForm(instance=label)
        return render(request, 'music/labels_update.html', context = { 'label_form': bound_form, 'label': label })

    def post(self, request, slug):
        label = Label.objects.get(slug__iexact=slug)
        bound_form = LabelForm(request.POST, instance=label)

        if bound_form.is_valid():
            new_label = bound_form.save()
        return redirect('labels_update_url', slug)


class LabelsDelete(View):
    def get(self, request, slug):
        label = Label.objects.get(slug__iexact=slug)
        return render(request, 'music/labels_delete.html', context = { 'label': label })

    def post(self, request, slug):
        label = Label.objects.get(slug__iexact=slug)
        label.delete()

        return redirect('labels_list_url')


class ProducersList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        sort = request.GET.getlist('sort')
        if search_query:
            producers = Producer.objects.filter(Q(producer_title__icontains=search_query) | Q(producer_bio__icontains=search_query))
        else:
            producers = Producer.objects.all().order_by(*sort)
        return render(request, 'music/producers_list.html', context = { 'producers': producers })


class ProducersDetail(View):
    def get(self, request, slug):
        producer = Producer.objects.get(slug__iexact=slug)
        return render(request, 'music/producers_detail.html', context = { 'producer': producer })

def time_float(time):
    if time == None:
        return 0
    else: 
        return (time.hour*60*60)+(time.minute*60)+time.second

class Charts(View):
    def get(self, request):
        country_chart = pygal.Pie(width=700, height=300, style=CleanStyle)
        all_albums = len(Album.objects.all())
        for i in range(len(Country.objects.all())):
            country_id = Country.objects.all()[i].country_id
            country_title = Country.objects.all()[i].country_title
            country_chart.add(country_title, len(Album.objects.filter(country__exact=country_id)))
        country_chart = country_chart.render(disable_xml_declaration=True)

        genre_chart = pygal.Bar(width=700, height=300, style=CleanStyle)
        all_songs = len(Song.objects.all())
        all_songs_without_genres = len(Song.objects.filter(genre_id__exact=None))
        for i in range(len(Genre.objects.all())):
            genre_id = Genre.objects.all()[i].genre_id
            genre_title = Genre.objects.all()[i].genre_title
            genre_chart.add(genre_title, len(Song.objects.filter(genre__exact=genre_id)))
        genre_chart = genre_chart.render(disable_xml_declaration=True)
        
        time_chart = pygal.Line(width=700, height=300, style=CleanStyle)
        songs = Song.objects.exclude(song_time__exact=None).order_by('-song_id')[:1000]
        songs_time = [0.0]*len(songs)
        all_songs_without_time = len(Song.objects.filter(song_time__exact=None))
        for i in range(len(songs)):
            songs_time[i] = time_float(songs[i].song_time)

        time_chart.add('Время (сек.)', songs_time[::-1])
        time_chart = time_chart.render(disable_xml_declaration=True)

        all_albums_without_labels = len(Album.objects.filter(label__exact=None))
        label_chart = pygal.HorizontalBar(width=700, height=300, style=CleanStyle)
        for i in range(len(Label.objects.all())):
            label_id = Label.objects.all()[i].label_id
            label_title = Label.objects.all()[i].label_title
            label_chart.add(label_title, len(Album.objects.filter(label__exact=label_id)))
        label_chart = label_chart.render(disable_xml_declaration=True)

        context = {
            'all_albums': all_albums,
            'all_songs': all_songs,
            'all_songs_without_genres': all_songs_without_genres,
            'all_songs_without_time': all_songs_without_time,
            'all_albums_without_labels': all_albums_without_labels,
            'country_chart': country_chart,
            'genre_chart': genre_chart,
            'time_chart': time_chart,
            'label_chart': label_chart,
        }

        return render(request, 'music/charts.html', context)
