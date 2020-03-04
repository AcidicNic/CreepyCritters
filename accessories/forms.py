from django.forms import ModelForm
from .views import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'info', 'price', 'item_img']
