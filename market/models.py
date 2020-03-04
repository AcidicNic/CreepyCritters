from string import ascii_letters, digits
from random import choice

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from django_currentuser.db.models import CurrentUserField


class Listing(models.Model):
    """ A single critter listing """
    slug = models.CharField(max_length=21, blank=True, editable=False,
                            help_text="Unique URL path to access this listing.")
    created_by = CurrentUserField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    name = models.CharField(max_length=settings.CRITTER_NAME_LENGTH, help_text="Critter's Name")
    title = models.CharField(max_length=settings.LISTING_TITLE_LENGTH, default="", help_text="Listing Title")
    desc = models.TextField(blank=True, default='', help_text="Describe your critter!")
    category = models.CharField(max_length=12, choices=settings.CRITTER_TYPES, default='???', help_text="Critter Type")
    species = models.CharField(max_length=24, help_text="Critter Species")
    age = models.IntegerField(blank=True, null=True, help_text="Critter Age")
    age_Format = models.CharField(blank=True, null=True, max_length=6,
                                  choices=[('Year', 'Year'), ('Years', 'Years'), ('Months', 'Months')], help_text="Year/Month")
    sex = models.CharField(blank=True, null=True, max_length=1,
                           choices=[('F', 'Female'), ('M', 'Male'), ('?', 'Unknown')], help_text="Critter Gender")
    price = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, help_text="Price (USD)")
    critter_img = models.ImageField(blank=True, null=True, upload_to='')

    def __str__(self):
        return f"{self.name}, the {self.species}"

    def get_absolute_url(self):
        """ Returns path for a listing """
        path_components = {'slug': self.slug}
        return reverse('show_critter', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates slug automatically when a listing is created """
        if not self.pk:
            self.slug = slugify(self.name+" "+''.join(choice(ascii_letters + digits) for _ in range(4)), allow_unicode=True)

        # Call save on the superclass.
        return super(Listing, self).save(*args, **kwargs)
