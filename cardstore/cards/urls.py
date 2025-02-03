

from django.urls import path, include
# this imports all the views from the views.py
from . import views
from .views import SearchResultsView



urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    # this is the home url
    path('', views.home, name='home'),
    # this is the single card url
    path('card-detail/<str:id>/', views.card_detail, name='card-detail'),
    # this is the add card url
    path('add-card/', views.add_card, name='add-card'),
    # this is the edit card url
    path('edit-card/<str:id>/', views.edit_card, name='edit-card'),
    # this is the delete card url
    path('delete-card/<str:id>/', views.delete_card, name='delete-card'),

    
]