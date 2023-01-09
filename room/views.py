from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden

from .models import Room, Message
from .forms import RoomForm

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


@login_required
# seul l'administrateur peut creer le salon 
def createroom(request):
    if request.user.is_superuser:
        if request.method=="POST":
            form=RoomForm(request.POST)
            if form.is_valid(): 
                room=form.save()
                return redirect("rooms") 
        form=RoomForm()
        return render(request, 'room/createroom.html',{"form":form})
    else:
        return render(request, 'room/error.html', {"error": "Vous n'êtes pas autorisé à créer le salon de discussion"})

@login_required
def delete_room(request, slug):
    #Autoriser uniquement les administrateurs à supprimer les salons de discussion
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    room = Room.objects.get(slug=slug)
    room.delete()

    return redirect('rooms')

      