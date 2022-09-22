from django import forms

from .models import Treat


class TreatForm(forms.ModelForm):
    img_upload = forms.FileField(required=False, label="Upload an image")

    class Meta:
        model = Treat
        fields = ['title', 'description', 'img_upload', 'rating']
        labels = {'title': 'title', 'description': 'description', 'cover_img': 'cover_img', 'rating': 'rating'}
