from django.shortcuts import render, get_object_or_404
from .models import Hotel

def liste_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/liste_hotels.html', {'hotels': hotels})

def detail_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    chambres = hotel.chambres.all()  # récupère toutes les chambres liées
    return render(request, 'hotel/detail_hotel.html', {'hotel': hotel, 'chambres': chambres})
