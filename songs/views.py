from django.shortcuts import render
from .models import Song
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import SongSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def fav_song(request):
    
    song = Song()

    if request.method == 'POST':
        print(request.data)
        song.song_id = int(request.data['id'])
        song.save()
        
    serialized_song = SongSerializer(song)
    return Response(serialized_song.data)


@api_view(['GET','POST'])
def fav_list(request):
        
    songs = Song.objects.all()

    serialized_songs = SongSerializer(songs, many=True)
    return Response(serialized_songs.data)


@api_view(['GET','POST'])
def unfav(request):

    if request.method == 'POST':
        id = int(request.data['id'])
        all_songs = Song.objects.all()
        for song in all_songs:
            if song.song_id == id:
                song.delete()
        serialized_song = SongSerializer(all_songs, many=True)
    return Response(serialized_song.data)


@api_view(['GET','POST'])
def delete_fav(request):

    if request.method == 'POST':
        id = int(request.data['id'])
        song = Song.objects.get(id=id)
        song.delete()
        all_songs = Song.objects.all()
        serialized_song = SongSerializer(all_songs, many=True)
    return Response(serialized_song.data)