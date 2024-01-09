from django.forms import ModelForm
from . models import movie_data

class movie_form(ModelForm):
    class Meta:
        model=movie_data
        fields='__all__'
