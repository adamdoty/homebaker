from django import forms

from .models import Treat, Note, Coupon


class TreatForm(forms.ModelForm):
    img_upload = forms.FileField(required=False, label="Upload an image")

    class Meta:
        model = Treat
        fields = ['title', 'description', 'img_upload', 'rating', 'recipe_source']
        labels = {'title': 'Title', 'description': 'Description', 'cover_img': 'Cover_img', 'rating': 'Rating',
                  'recipe_source': 'Recipe source'}


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['body']
        labels = {'body': 'Note content'}


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['reason', 'recipient', 'treat', 'target_date', 'expiration_date']
        labels = {'reason': 'Reason for Coupon', 'recipient': 'Coupon Recipient', 'treat': 'Treat', 'target_date': 'Date of Event/Coupon Reason', 'expiration_date': 'Expiration Date'}
