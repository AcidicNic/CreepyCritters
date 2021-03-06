from django.forms import ModelForm
from .models import Listing


class CritterForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'title', 'category', 'species', 'age', 'sex', 'age_Format', 'price', 'desc', 'critter_img']