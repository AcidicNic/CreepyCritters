from django.forms import ModelForm
from .models import Listing


class ArticleForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'desc', 'type', 'species', 'critter_img']
