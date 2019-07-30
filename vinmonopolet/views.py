from django.shortcuts import render
from .modules import cheapest
from .forms import VinmonopoletForm

def vinmonopolet(request):
    if request.method == 'POST':
        form = VinmonopoletForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            alcohol_type = form.cleaned_data['alcohol_type']
            context = cheapest(alcohol_type, number)
            return render(request, 'vinmonopolet/calculator.html', {'data': context,
                                                                    'form': form, 'number': number,
                                                                    'alcohol_type': alcohol_type})
    else:
        form = VinmonopoletForm()
    return render(request, 'vinmonopolet/calculator.html', {'form': form, 'title': 'Vinmonopolet Calculator'})

