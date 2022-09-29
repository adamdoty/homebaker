from django.forms import DateInput, ModelForm, FileField

from .models import Treat, Note, Coupon


class TreatForm(ModelForm):
    img_upload = FileField(required=False, label="Upload an image")

    class Meta:
        model = Treat
        fields = ['title', 'description', 'img_upload', 'rating', 'recipe_source']
        labels = {'title': 'Title', 'description': 'Description', 'cover_img': 'Cover_img', 'rating': 'Rating',
                  'recipe_source': 'Recipe source'}


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['body']
        labels = {'body': 'Note content'}


class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = ['reason', 'recipient', 'target_date', 'expiration_date']
        labels = {'reason': 'Reason for Coupon', 'recipient': 'Coupon Recipient',
                  'target_date': 'Date of Event/Coupon Reason', 'expiration_date': 'Expiration Date'}
        widgets = {
            'target_date': DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
            'expiration_date': DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
        }
