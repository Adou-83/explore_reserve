from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_hotels, name='liste_hotels'),
    path('<int:hotel_id>/', views.detail_hotel, name='detail_hotel'),
]
