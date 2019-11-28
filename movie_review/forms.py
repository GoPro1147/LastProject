from django import forms
from .models import Review, Movie


class ReviewForm(forms.ModelForm):
    class Meta():
        model = Review
        fields = ('content', 'rating', )



class MovieForm(forms.ModelForm):
    class Meta():
        model = Movie
        fields = ('title', 'openDt', 'genres', 'actors', 'mvdirector', 'img_url', 'description',)