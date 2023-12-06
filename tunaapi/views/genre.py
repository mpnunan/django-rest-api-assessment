from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre


class GenreView(ViewSet):

    def retrieve(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        except Genre.DoesNotExist as ex:
            return Response({'message', ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
            model = Genre
            fields = ('id', 'description')
