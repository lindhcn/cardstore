
from django import forms
from .forms import EditcardForm

from django.shortcuts import render, redirect

from .models import Card

from django.http import HttpResponse

from django.views.generic import TemplateView, ListView

from django.db.models import Q


class SearchResultsView(ListView):
    model = Card
    template_name = 'cards/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Card.objects.filter(
            Q(player__icontains=query) | Q(player__icontains=query)
        )
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("q")
        return context
    
sortchoices = (("asc", "Ascending A-Z"), ("desc", "descending Z-A"))

class sortform(forms.Form):
    sortby = forms.ChoiceField(
        choices = sortchoices,
        widget=forms.Select(attrs={'onchange': 'myfunction()'}))
    def __init__(self, *args, **kwargs):
        if 'my_initial' in kwargs:
            init_val = kwargs.pop('my_initial')
        else:
            init_val = 1
        super().__init__(*args, **kwargs)
        self.initial['sortby'] = init_val


# this is a view for listing all the cards
def home(request):
    # retrieving all the cards from the database
    sort_by = request.GET.get("sortby")

    sort_f = sortform(my_initial = sort_by)
    print (sort_f)

    if sort_by == "asc":
        cards = Card.objects.all().order_by('player')
    else:
        cards = Card.objects.all().order_by('-player')

    context = {'cards': cards, 'sort_f': sort_f}
    return render(request, 'cards/home.html', context)

# this is a view for listing a single card,it will take id as an argument
def card_detail(request, id):
    # querying a particular card by its id
    card = Card.objects.get(pk=id)
    context = {'card': card}
    return render(request, 'cards/card-detail.html', context)

# this is a view for adding a card
def add_card(request):
    # checking if the method is POST
    if request.method == 'POST':
        # getting all the data from the POST request
        data = request.POST
        # getting the image
        image = request.FILES.get('image-file')
        # creating and saving the card
        card = Card.objects.create(
           player = data['player'],
           series = data['series'],
           year = data['year'],
           index = data['index'],
           image = image
        )
        # going to the home page
        return redirect('home')
    return render(request, 'cards/add-card.html')

# this is a view for editing the card's info
def edit_card(request, id):
    # getting the card to be updated
    card = Card.objects.get(pk=id)
    # populating the form with the card's information
    form = EditcardForm(instance=card)
    # checking if the request is POST
    if request.method == 'POST':
        # filling the form with all the request data 
        form = EditcardForm(request.POST, request.FILES, instance=card)
        # checking if the form's data is valid
        if form.is_valid():
            # saving the data to the database
            form.save()
            # redirecting to the home page
            return redirect('home')
    context = {'form': form}
    return render(request, 'cards/update-card.html', context)

# this is a view for deleting a card,it will take id as an argument
# this is a view for deleting a card
def delete_card(request, id):
    # getting the card to be deleted
    card = Card.objects.get(pk=id)
    # checking if the method is POST
    if request.method == 'POST':
        # delete the card
        card.delete()
        # return to home after a success delete
        return redirect('home')
    context = {'card': card}
    return render(request, 'cards/delete-card.html', context)
