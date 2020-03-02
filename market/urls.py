from django.urls import path
from .views import CritterListView, CritterDetailView, AddCritter, DeleteCritter, profile
from django.conf import settings

urlpatterns = [
    # New Listing Form
    path('addListing/', AddCritter.as_view(), name='createListing'),

    # URLs for every critter type (defined in settings!)
    # path(r'bois/(?P<critterType>' + '|'.join(settings.CRITTER_TYPE_URLS) + ')/',
    #      CritterListView.as_view(), name='list_critters'),

    # URLs for every critter type (defined in settings!)
    path('', CritterListView.as_view(), name='list_critters'),

    # Display a single boi's listing
    path('boi/<str:slug>',
         CritterDetailView.as_view(), name='show_critter'),

    path(r'delete/<pk>/', DeleteCritter.as_view(), name='delete_critter'),

    path(r'profile/<username>/', profile, name='profile')
]
