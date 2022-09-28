from django import forms

from .models import Treat, Note


class TreatForm(forms.ModelForm):
    img_upload = forms.FileField(required=False, label="Upload an image")

    class Meta:
        model = Treat
        fields = ['title', 'description', 'img_upload', 'rating']
        labels = {'title': 'Title', 'description': 'Description', 'cover_img': 'Cover_img', 'rating': 'Rating'}


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['body']
        labels = {'body': 'Note content'}
