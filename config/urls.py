from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_app.urls')),             # page d'accueil ici
    path('hotels/', include('hotel.urls')),         # App 2
    path('reservations/', include('reserve.urls')), # App 3
]
