from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.liste_hotels, name='liste_hotels'),
    path('<int:pk>/', views.detail_hotel, name='detail_hotel'),
    path('chambres/', views.liste_chambres, name='liste_chambres'),
    path('chambres/<int:pk>/', views.detail_chambre, name='detail_chambre'),
]
