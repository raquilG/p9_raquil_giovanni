from django import forms

from . import models


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['user', 'followed_user']
