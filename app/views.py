from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Flavor, Ingredient, CustomerSuggestion
from django.db import IntegrityError 
# Create your views here.

def home(request):
    return render(request, 'home.html')


def add_flavor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        season = request.POST.get('season')

        if not name:
            return render(request, 'add_flavor.html', {'error': 'Flavor name cannot be empty.'})

        name = name.strip().lower()

        if not season:
            return render(request, 'add_flavor.html', {'error': 'Season cannot be empty.'})

        if Flavor.objects.filter(name=name).exists():
            return render(request, 'add_flavor.html', {'error': 'Flavor already exists.'})

        try:
            Flavor.objects.create(name=name, season=season)
            return redirect('view_flavors')
        except IntegrityError:
            return render(request, 'add_flavor.html', {'error': 'An error occurred when saving the flavor.'})

    return render(request, 'add_flavor.html')



def view_flavors(request):
    flavors = Flavor.objects.all()
    return render(request, 'view_flavors.html', {'flavors': flavors})


def update_flavor(request, flavor_id):
    flavor = get_object_or_404(Flavor, id=flavor_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        season = request.POST.get('season')

        if not name:
            return render(request, 'update_flavor.html', {'flavor': flavor, 'error': 'Flavor name cannot be empty.'})

        name = name.strip().lower()

        if not season:
            return render(request, 'update_flavor.html', {'flavor': flavor, 'error': 'Season cannot be empty.'})

        try:
            flavor.name = name
            flavor.season = season
            flavor.save()
            return redirect('view_flavors')
        except IntegrityError:
            return render(request, 'update_flavor.html', {'flavor': flavor, 'error': 'Flavor already exists.'})

    return render(request, 'update_flavor.html', {'flavor': flavor})



def add_ingredient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')

        if not name or not quantity:
            return render(request, 'add_ingredient.html', {'error': 'Name and quantity are required.'})

        try:
            name = name.strip().lower()
            quantity = int(quantity)

            if quantity < 0:
                return render(request, 'add_ingredient.html', {'error': 'Quantity cannot be negative.'})

            Ingredient.objects.create(name=name, quantity=quantity)
            return redirect('view_ingredients')
        except ValueError:
            return render(request, 'add_ingredient.html', {'error': 'Quantity must be a valid number.'})
        except IntegrityError:
            return render(request, 'add_ingredient.html', {'error': 'Ingredient already exists.'})

    return render(request, 'add_ingredient.html')


def view_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'view_ingredients.html', {'ingredients': ingredients})

def update_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')

        if not name or not quantity:
            return render(request, 'update_ingredient.html', {'ingredient': ingredient, 'error': 'Name and quantity are required.'})

        try:
            name = name.strip().lower()
            quantity = int(quantity)

            if quantity < 0:
                return render(request, 'update_ingredient.html', {'ingredient': ingredient, 'error': 'Quantity cannot be negative.'})

            ingredient.name = name
            ingredient.quantity = quantity
            ingredient.save()
            return redirect('view_ingredients')
        except ValueError:
            return render(request, 'update_ingredient.html', {'ingredient': ingredient, 'error': 'Quantity must be a valid number.'})
        except IntegrityError:
            return render(request, 'update_ingredient.html', {'ingredient': ingredient, 'error': 'Ingredient already exists.'})

    return render(request, 'update_ingredient.html', {'ingredient': ingredient})



def add_suggestion(request):
    if request.method == 'POST':
        flavor_suggestion = request.POST.get('flavor_name')
        allergy_concern = request.POST.get('allergy_concern')

        if not flavor_suggestion:
            return render(request, 'add_suggestion.html', {'error': 'Flavor name is required.'})
        
        if not allergy_concern:
            allergy_concern = "No allergy concerns"
            
        try:
            flavor_suggestion = flavor_suggestion.strip().lower()

            CustomerSuggestion.objects.create(flavor_suggestion=flavor_suggestion, allergy_concern=allergy_concern)
            return redirect('view_suggestions')
        except IntegrityError:
            return render(request, 'add_suggestion.html', {'error': 'Suggestion with this flavor already exists.'})

    return render(request, 'add_suggestion.html')



def view_suggestions(request):
    suggestions = CustomerSuggestion.objects.all()
    return render(request, 'view_suggestions.html', {'suggestions': suggestions})
