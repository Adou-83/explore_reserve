from django import forms
from .models import Lieu

class LieuForm(forms.ModelForm):
    class Meta:
        model = Lieu
        fields = ['nom', 'description', 'adresse', 'ville', 'image']
