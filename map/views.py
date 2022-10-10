from django.shortcuts import render
from .models import *

def home(request):
    cafes = Cafe.objects.all()
    test = Cafe.objects.all()[0]
    return render(request, 'map/home.html', {'cafes': cafes, 'test': test,})
