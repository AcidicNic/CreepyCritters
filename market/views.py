from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import AddCritterForm, EditCritterForm
from .models import Listing
from accessories.models import Item


class CreepyCrittersHome(TemplateView):
    """ List all critters and Shop Items """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(CreepyCrittersHome, self).get_context_data(**kwargs)
        context['listings'] = Listing.objects.get_queryset().all()
        context['items'] = Item.objects.get_queryset().all()
        return context


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
    form_class = AddCritterForm
    template_name = 'market/add_form.html'


class DeleteCritter(LoginRequiredMixin, DeleteView):
    model = Listing
    success_url = reverse_lazy('critter_home')
    template_name = 'market/confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        """ Only superusers and listing owners can delete """
        listing = self.get_object()
        if listing.created_by != self.request.user:
            if not self.request.user.is_superuser:
                return redirect(listing)
        return super(DeleteCritter, self).dispatch(request, *args, **kwargs)


class EditCritter(LoginRequiredMixin, UpdateView):
    model = Listing
    form_class = EditCritterForm
    template_name = 'market/edit_form.html'

    def dispatch(self, request, *args, **kwargs):
        """ Only superusers and listing owners can edit """
        critter = self.get_object()
        if not critter.created_by == self.request.user:
            if not self.request.user.is_superuser:
                return redirect(critter)
        return super(EditCritter, self).dispatch(request, *args, **kwargs)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    listings = Listing.objects.filter(created_by=user)

    return render(request, 'market/profile.html', {'this_user': user, 'listings': listings})
