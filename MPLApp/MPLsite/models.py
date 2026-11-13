from django.db import models
from django.contrib.auth.models import User

# models

class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "playlists")
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    
    def __str__ (self):
        return f"{self.title} - {self.artist}"   
