from django import forms
from .models import HarryWinstonPiece

class EstimateValueForm(forms.ModelForm):
    class Meta:
        model = HarryWinstonPiece
        fields = ('model_name', 'serial_number', 'style', 'materials', 'features', 'documentation', 'condition')