from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Item
from .forms import ItemForm


class ShopHome(ListView):
    """ Renders a list of all Pages. """
    model = Item

    def get(self, request):
        """ GET a list of Pages. """
        items = self.get_queryset().all()
        return render(request, 'shop/home.html', {
            'items': items
        })


class ItemDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Item

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        item = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'shop/show_item.html', {
            'item': item
        })


class AddItem(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'shop/add_form.html'


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('shop_home')
    template_name = 'shop/confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        """ Only superusers and listing owners can delete """
        item = self.get_object()
        if not self.request.user.is_superuser:
            return redirect(item)
        return super(DeleteItem, self).dispatch(request, *args, **kwargs)


class EditItem(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'shop/edit_form.html'

    def dispatch(self, request, *args, **kwargs):
        """ Only superusers and listing owners can edit """
        item = self.get_object()
        if not self.request.user.is_superuser:
            return redirect(item)
        return super(EditItem, self).dispatch(request, *args, **kwargs)
