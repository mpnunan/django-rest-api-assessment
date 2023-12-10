from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist, SongGenre
from .genre import GenreSerializer


class SongView(ViewSet):
  
    def retrieve(self, request, pk):
        try:
            song = Song.objects.get(pk=pk)
            serializer = SongDetailsSerializer(song)
            return Response(serializer.data)
        except Song.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        songs = Song.objects.all()
        serializer = SongSerializerShallow(songs, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        artist = Artist.objects.get(pk=request.data["artist_id"])
        song = Song.objects.create(
            title=request.data["title"],
            artist=artist,
            album=request.data["album"],
            length=request.data["length"]
        )
        serializer = SongSerializerShallow(song)
        return Response(serializer.data)
    
    def update(self, request, pk):
        artist = Artist.objects.get(pk=request.data["artist_id"])
        song = Song.objects.get(pk=pk)
        song.title=request.data["title"]
        song.artist=artist
        song.album=request.data["album"]
        song.length=request.data["length"]
        song.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album', 'length')
        depth = 1

class SongSerializerShallow(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist_id', 'album', 'length')
        
class SongDetailsSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album', 'length', 'genres')
        depth = 1
