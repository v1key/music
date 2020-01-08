from django.db import models
from django.utils.text import slugify
from django.db.models.functions import TruncMinute
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_title = models.CharField(max_length=50)
    album_type = models.ForeignKey('AlbumType', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    producer = models.ForeignKey('Producer', models.DO_NOTHING, blank=True, null=True)
    label = models.ForeignKey('Label', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    class Meta:
        managed = False
        db_table = 'album'
        ordering = ["album_id"]  

    def __str__(self):
        return self.album_title

    def save(self, *args, **kwargs):
        if not self.album_id:
            self.slug = gen_slug(self.album_title)
        super(Album, self).save(*args, **kwargs)


class AlbumType(models.Model):
    album_type_id = models.AutoField(primary_key=True)
    album_type_title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'album_type'

    def __str__(self):
        return self.album_type_title


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_title = models.CharField(max_length=50)
    artist_bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)


    class Meta:
        managed = False
        db_table = 'artist'

    def __str__(self):
        return self.artist_title

    def save(self, *args, **kwargs):
        if not self.artist_id:
            self.slug = gen_slug(self.artist_title)
        super(Artist, self).save(*args, **kwargs)


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_title = models.CharField(max_length=50)
    author_bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    class Meta:
        managed = False
        db_table = 'author'

    def __str__(self):
        return self.author_title

    def save(self, *args, **kwargs):
        if not self.author_id:
            self.slug = gen_slug(self.author_title)
        super(Author, self).save(*args, **kwargs)

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country_title


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_title = models.CharField(max_length=50)
    genre_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    class Meta:
        managed = False
        db_table = 'genre'

    def __str__(self):
        return self.genre_title

    def save(self, *args, **kwargs):
        if not self.genre_id:
            self.slug = gen_slug(self.genre_title)
        super(Genre, self).save(*args, **kwargs)


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_title = models.CharField(max_length=50)
    label_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    class Meta:
        managed = False
        db_table = 'label'

    def __str__(self):
        return self.label_title

    def save(self, *args, **kwargs):
        if not self.label_id:
            self.slug = gen_slug(self.label_title)
        super(Label, self).save(*args, **kwargs)


class Producer(models.Model):
    producer_id = models.AutoField(primary_key=True)
    producer_title = models.CharField(max_length=50)
    producer_bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    class Meta:
        managed = False
        db_table = 'producer'

    def __str__(self):
        return self.producer_title

    def save(self, *args, **kwargs):
        if not self.producer_id:
            self.slug = gen_slug(self.producer_title)
        super(Producer, self).save(*args, **kwargs)


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_title = models.CharField(max_length=50)
    song_time = models.TimeField(blank=True, null=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, blank=True, null=True)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)
    genre = models.ForeignKey(Genre, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song'

    def __str__(self):
        return self.song_title

class SongAuthors(models.Model):
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    song = models.ForeignKey(Song, models.DO_NOTHING, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'song_authors'


