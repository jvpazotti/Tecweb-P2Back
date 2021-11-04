from django.shortcuts import render
from .models import Song
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import SongSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def api_note(request, song_id):
    try:
        song = Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        song.song_id = song_id
        song.save()


    serialized_song = SongSerializer(song)
    return Response(serialized_song.data)

@api_view(['GET','POST'])

def api_note_list(request):

    if request.method == "POST":
        new_note_data = request.data
        note = Song()
        note.title = new_note_data["title"]
        note.content = new_note_data["content"]
        note.save()
        
    notes= Song.objects.all()

    serialized_notes = SongSerializer(notes,many=True)
    return Response(serialized_notes.data)
