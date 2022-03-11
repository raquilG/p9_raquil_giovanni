from django import forms

from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    CHOICES = [('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
    rating = forms.ChoiceField(label="Note", choices=CHOICES, widget=forms.RadioSelect)
    header = forms.CharField(label="Titre", widget=forms.TextInput)
    body = forms.CharField(label="commentaire", widget=forms.Textarea)

    class Meta:
        model = models.Review
        fields = ['header', 'rating', 'body']
