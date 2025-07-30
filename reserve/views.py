from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

@login_required
def liste_reservations(request):
    # Montrer les réservations du client connecté
    reservations = Reservation.objects.filter(client=request.user)
    return render(request, 'reserve/liste_reservations.html', {'reservations': reservations})

@login_required
def ajouter_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.client = request.user
            reservation.statut = 'en_attente'
            reservation.save()
            return redirect('liste_reservations')
    else:
        form = ReservationForm()
    return render(request, 'reserve/ajouter_reservations.html', {'form': form})
