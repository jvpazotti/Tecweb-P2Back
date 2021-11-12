from django.shortcuts import render
from .models import Song
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import SongSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def fav_song(request):
    


    if request.method == 'POST':
        song = Song()
        print(request.data)
        song.song_id = int(request.data['song_id'])
        song.save()
        print("PASSOUUU")


    serialized_song = SongSerializer(song)
    return Response(serialized_song.data)

@api_view(['GET','POST'])

def fav_list(request):

    # if request.method == "POST":
    #     new_note_data = request.data
    #     note = Song()
    #     note.title = new_note_data["title"]
    #     note.content = new_note_data["content"]
    #     note.save()
        
    songs = Song.objects.all()

    serialized_songs = SongSerializer(songs, many=True)
    return Response(serialized_songs.data)

@api_view(['GET','POST','DELETE'])

def delete_fav(request):

    print(request.data)
    if request.method == 'POST':
        id = int(request.data['id'])
        song = Song.objects.get(id=id)
        song.delete()
        all_songs = Song.objects.all()
        serialized_song = SongSerializer(all_songs, many=True)
    return Response(serialized_song.data)


