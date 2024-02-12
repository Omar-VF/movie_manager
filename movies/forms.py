from django.forms import ModelForm
from django import forms
from .models import movie_data


class movie_form(ModelForm):
    class Meta:
        model = movie_data
        fields = "__all__"


class MovieSearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100)
