from django.shortcuts import render
from .models import Playlist

# views

def home(request):
    playlists = Playlist.objects.filter(is_public=True).order_by("-created_at")[:10]
    return render(request, "home.html", {"playlists": playlists})

