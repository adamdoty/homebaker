from django import forms

from .models import Treat


class TreatForm(forms.ModelForm):
    class Meta:
        model = Treat
        fields = ['title', 'description', 'cover_img', 'rating']
        labels = {'title': 'title', 'description': 'description', 'cover_img': 'cover_img', 'rating': 'rating'}
