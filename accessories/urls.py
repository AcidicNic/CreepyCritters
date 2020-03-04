from django.urls import path
from .views import ShopHome, ItemDetailView, AddItem, EditItem, DeleteItem

urlpatterns = [
    # All Critters / Home Page
    path('', ShopHome.as_view(), name='shop_home'),
    path('item/<slug>/', ItemDetailView.as_view(), name='show_item'),
    path('add/', AddItem.as_view(), name='add_item'),
    path('edit/<slug>/', EditItem.as_view(), name='edit_item'),
    path('delete/<slug>/', DeleteItem.as_view(), name='delete_item'),
]