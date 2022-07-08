from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def Home(request):
    return render(request, 'Home.html')


def Rooms(request):
    return render(request, 'Room.html')
