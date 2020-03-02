from django.forms import ModelForm
from .models import Listing


class CritterForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'desc', 'type', 'species', 'critter_img']
