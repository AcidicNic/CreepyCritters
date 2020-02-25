from django.forms import ModelForm
from .models import Listing


class ArticleForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'desc', 'type', 'species']
