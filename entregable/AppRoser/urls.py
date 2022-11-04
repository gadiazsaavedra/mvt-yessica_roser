from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crear/', views.crear),
    path('crear/<nombre>/', views.crear),
    path('crear/<nombre>/<apellido>/', views.crear),
    path('crear/<nombre>/<apellido>/<edad>/', views.crear),
    path('crear/<nombre>/<apellido>/<edad>/<parentesco>', views.crear),
    path('mostrar/', views.mostrar),
]