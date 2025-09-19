from django import forms
from .models import Reservation
from hotel.models import Chambre

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['chambre', 'date_arrivee', 'date_depart']
        widgets = {
            'date_arrivee': forms.DateInput(attrs={'type': 'date'}),
            'date_depart': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['chambre'].queryset = Chambre.objects.all()
