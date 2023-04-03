# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def diga_oi(request):
  # Buscar dados de base
  # Manipular dados
  # Mandar emails...
  return render(request, 'oi.html')