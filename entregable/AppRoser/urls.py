from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crear/', views.crear),
    path('crear/<nombre>/', views.crear),
    path('crear/<nombre>/<apellido>/', views.crear),
    path('crear/<nombre>/<apellido>/<dni>/', views.crear),
    path('mostrar/', views.mostrar),
]