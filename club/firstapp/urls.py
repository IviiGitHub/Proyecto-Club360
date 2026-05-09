from django.urls import path
from . import views

urlpatterns = [
    path('', views.seccion_reservas, name='seccion_reservas'),
]