from django.urls import path
from .views import CritterListView, CritterDetailView, AddCritter, EditCritter, DeleteCritter, profile, CreepyCrittersHome
from django.conf import settings

urlpatterns = [
    # Home Page
    # path('', CreepyCrittersHome.as_view(), name='home'),

    # All Critters
    path('', CritterListView.as_view(), name='critter_home'),

    # TODO: URLs for every critter type
    path(r'critters/<str:type>', CritterListView.as_view(), name='critter_type'),
    # TODO: Search for critters
    path(r'critters/search/<str:type>', CritterListView.as_view(), name='critter_search'),

    # Display a single boi's listing
    path('boi/<str:slug>',
         CritterDetailView.as_view(), name='show_critter'),
    # New Listing Form
    path('add/', AddCritter.as_view(), name='add_critter'),
    # Edit Listing
    path('edit/<slug>/', EditCritter.as_view(), name='edit_critter'),
    # Delete Listing
    path(r'delete/<slug>/', DeleteCritter.as_view(), name='delete_critter'),

    # User Profile page!
    path(r'profile/<username>/', profile, name='profile')
]
