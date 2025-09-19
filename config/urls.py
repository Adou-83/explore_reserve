from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core app
    path('', include(('core_app.urls', 'core_app'), namespace='core_app')),

    # Django auth (login/logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # Hotel app
    path('hotels/', include(('hotel.urls', 'hotel'), namespace='hotel')),

    # Réservations
    path('reservations/', include(('reserve.urls', 'reserve'), namespace='reserve')),
]

# Pour servir les fichiers media en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
