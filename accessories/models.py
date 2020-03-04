from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_currentuser.db.models import CurrentUserField
from random import choice
from string import ascii_letters, digits


class Item(models.Model):
    slug = models.CharField(max_length=32, blank=True, editable=False)
    created_by = CurrentUserField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=32, default="", help_text="Item Title")
    info = models.TextField(help_text="Extra information about this item.")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Price (USD)")
    item_img = models.ImageField(upload_to='')

    def __str__(self):
        return f"{self.title} (#{self.pk})"

    def get_absolute_url(self):
        """ Returns path for a listing """
        path_components = {'slug': self.slug}
        return reverse('show_item', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates slug automatically when a listing is created """
        if not self.pk:
            self.slug = slugify(f"{self.title} {''.join(choice(ascii_letters + digits) for _ in range(3))}", allow_unicode=True)
        return super(Item, self).save(*args, **kwargs)
