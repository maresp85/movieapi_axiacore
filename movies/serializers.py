from rest_framework import serializers
from .models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)

'''GET, PUT, DELETE'''
class MovieSerializer(serializers.ModelSerializer):
    genre_id = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'overview','poster_path','original_title', 'original_language',
                  'title', 'release_date', 'rating', 'genre_id')

'''POST'''
class MovieSerializerP(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'overview','poster_path','original_title', 'original_language',
                  'title', 'release_date', 'rating', 'genre_id')
