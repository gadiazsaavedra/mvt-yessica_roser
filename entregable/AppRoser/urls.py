from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crear-familiar/', views.crear-familiar),
    path('crear-familiar/<nombre>/', views.crear-familiar),
    path('crear-familiar/<nombre>/<apellido>/', views.crear-familiar),
    path('crear-familiar/<nombre>/<apellido>/<edad>/', views.crear-familiar),
    path('crear-familiar/<nombre>/<apellido>/<edad>/<parentesco>', views.crear-familiar),
    path('mostrar/', views.mostrar),
]