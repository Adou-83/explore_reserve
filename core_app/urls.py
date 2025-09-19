from django.urls import path
from . import views

app_name = 'core_app'

urlpatterns = [
    path('', views.accueil, name='accueil'),

    # Lieux
    path('lieux/', views.liste_lieux, name='liste_lieux'),
    path('lieux/<int:pk>/', views.detail_lieu, name='lieu_detail'),

    # Découvertes
    path('decouvertes/', views.page_decouverte, name='page_decouverte'),
    path('decouvertes/<int:pk>/', views.detail_decouverte, name='decouverte_detail'),

    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
