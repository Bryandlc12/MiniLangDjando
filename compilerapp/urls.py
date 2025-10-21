from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analizar/', views.analizar_codigo, name='analizar'),
]
