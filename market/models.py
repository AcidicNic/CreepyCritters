from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from django_currentuser.db.models import CurrentUserField


class Listing(models.Model):
    """ A single critter listing """
    title = models.CharField(max_length=settings.LISTING_TITLE_LENGTH, unique=True, help_text="Listing Title")
    created_by = CurrentUserField()
    slug = models.CharField(max_length=settings.LISTING_TITLE_LENGTH, blank=True, editable=False,
                            help_text="Unique URL path to access this listing.")
    desc = models.TextField(help_text="Describe your critter")
    created = models.DateTimeField(auto_now_add=True, help_text="The date & time this listing was created.")
    modified = models.DateTimeField(auto_now=True, help_text="The date & time this listing was updated.")

    type = models.CharField(max_length=12, choices=settings.CRITTER_TYPES, default='???', help_text="Critter Type")
    species = models.CharField(max_length=24, help_text="Critter Species")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns path for a listing """
        path_components = {'slug': self.slug}
        return reverse('show_critter', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates slug automatically when a listing is created """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Listing, self).save(*args, **kwargs)
