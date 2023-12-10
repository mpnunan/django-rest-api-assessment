from django.db import models

class Genre(models.Model):
  
    description = models.CharField(max_length=50)
    
    def songs(self):
        return [song_genre.song for song_genre in self.song_genres.all()]
