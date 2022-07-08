from django.shortcuts import redirect, render
from .models import Room
from .forms import RoomForm

# Create your views here.


def Home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/Home.html', context)


def Rooms(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/Room.html', context)


def createRoom(request):
    form = RoomForm()
    if(request.method == 'POST'):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/Form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if(request.method == 'POST'):
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/Form.html', context)
