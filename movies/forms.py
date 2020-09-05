from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('overview','poster_path','original_title', 'original_language',
                  'title', 'release_date', 'rating', 'genre_id')
