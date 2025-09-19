from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfilUtilisateur

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            ProfilUtilisateur.objects.create(
                utilisateur=user,
                telephone=self.cleaned_data['telephone']
            )
        return user
