# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_title = models.CharField(max_length=50)
    album_type = models.ForeignKey('AlbumType', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    producer = models.ForeignKey('Producer', models.DO_NOTHING, blank=True, null=True)
    label = models.ForeignKey('Label', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'


class AlbumType(models.Model):
    album_type_id = models.AutoField(primary_key=True)
    album_type_title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'album_type'


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_title = models.CharField(max_length=50)
    artist_bio = models.TextField(blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist'


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_title = models.CharField(max_length=50)
    author_bio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'country'


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_title = models.CharField(max_length=50)
    genre_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_title = models.CharField(max_length=50)
    label_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label'


class Producer(models.Model):
    producer_id = models.AutoField(primary_key=True)
    producer_title = models.CharField(max_length=50)
    producer_bio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producer'


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_title = models.CharField(max_length=50)
    song_time = models.TimeField()
    artist = models.ForeignKey(Artist, models.DO_NOTHING, blank=True, null=True)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)
    genre = models.ForeignKey(Genre, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song'


class SongAuthors(models.Model):
    song = models.ForeignKey(Song, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song_authors'
