from django.shortcuts import render
from .forms import PizzaForm


def calc_pizza(weight, water_percentage, number):
    total_weight = float(weight) * float(number)
    salt = round(float(total_weight) * 0.019,1)
    flour = int((total_weight) / (float(water_percentage) * 0.01 + 1))
    water = int(total_weight - flour)
    yeast = round(total_weight * 0.0012,1)
    return flour, water, salt, yeast


def pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            water_percentage = form.cleaned_data['water_percentage']
            number = form.cleaned_data['number']

            flour, water, salt, yeast = calc_pizza(weight, water_percentage, number)
            context = {'flour': flour, 'water': water, 'salt': salt,
                       'yeast': yeast, 'form': form, 'title': 'Pizzadough Calculator'}
            return render(request, 'pizza/pizzadough.html', context)
    else:
        form = PizzaForm()
    return render(request, 'pizza/pizzadough.html', {'form': form, 'title': 'Pizzadough Calculator'})
