from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import ArticleForm
from .models import Listing


class CritterListView(ListView):
    """ Renders a list of all Pages. """
    model = Listing

    def get(self, request):
        """ GET a list of Pages. """
        listings = self.get_queryset().all()
        return render(request, 'market/list_critters.html', {
            'listings': listings
        })


class CritterDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Listing

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        listing = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'market/show_critter.html', {
            'critter': listing
        })


class AddCritter(LoginRequiredMixin, CreateView):
    model = Listing
    form_class = ArticleForm
