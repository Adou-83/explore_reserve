from django.shortcuts import render, get_object_or_404
from .models import Hotel, Chambre

def liste_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/liste_hotel.html', {'hotels': hotels})

def detail_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    chambres = hotel.chambres.all()
    return render(request, 'hotel/detail_hotel.html', {'hotel': hotel, 'chambres': chambres})

def liste_chambres(request):
    chambres = Chambre.objects.all()
    return render(request, 'hotel/liste_chambres.html', {'chambres': chambres})

def detail_chambre(request, pk):
    chambre = get_object_or_404(Chambre, pk=pk)
    return render(request, 'hotel/detail_chambre.html', {'chambre': chambre})
