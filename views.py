from django.shortcuts import render
from .models import Pizza, Reservation
from .data import data , moor_data

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html', {'piz': Pizza.objects.all()})

def reservation(request):
    name = render.POST.get('name')
    positions = render.POST.get('position')
    p_chois = render.POST.get('chois')
    reservation = Reservation(person = name, position = positions, chois = p_chois)
    reservation.save()
    return render(request, 'reservation.html', {'data': data, 'moor_data': moor_data})