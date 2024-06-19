from django.shortcuts import render
from .forms import EstimateValueForm
from .models import HarryWinstonPiece

def estimate_value(request):
    if request.method == 'POST':
        form = EstimateValueForm(request.POST)
        if form.is_valid():
            # Process the form data and estimate the value
            # For now, just save the data to the database
            form.save()
            return render(request, 'estimate_value_result.html', {'message': 'Thank you for submitting your request!'})
    else:
        form = EstimateValueForm()
    return render(request, 'estimate_value.html', {'form': form})