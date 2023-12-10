from django.db import models
from .song import Song
from .genre import Genre

class SongGenre(models.Model):

    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="genre_songs")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="song_genres")
