from django.forms import DateInput, ModelForm, FileField, CharField, TextInput, Textarea
from django.contrib.auth.models import User

from .models import Treat, Note, Coupon, Profile


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


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('is_baker_user',)


class TreatRequestForm(ModelForm):
    """A form for recipient users to requests treats not in the treat catalogue."""
    title = CharField(widget=TextInput(attrs={'placeholder': 'i.e. Buckeyes'}))
    description = CharField(widget=Textarea(attrs={'placeholder': 'i.e. Peanut butter balls coated in chocolate'}))
    recipe_source = CharField(widget=Textarea(
        attrs={'placeholder': 'i.e. Duff Bakes '
                              '\nor '
                              '\nhttps://www.amazon.com/Duff-Bakes-Think-Bake-Like/dp/0062349805'
                              '\nor '
                              '\nhttps://www.yahoo.com/entertainment/buckeyes-from-duff-bakes-1326919478968374.html'}))

    class Meta:
        model = Treat
        fields = ['title', 'description', 'recipe_source']
        labels = {'title': 'Title', 'description': 'Description', 'recipe_source': 'Recipe Source'}
