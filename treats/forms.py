from django import forms

from .models import Treat


class TreatForm(forms.ModelForm):
    class Meta:
        model = Treat
        fields = ['name', 'recipe_link', 'picture_link']
        labels = {'name': 'treat', 'recipe_link': '', 'picture_link': ''}
