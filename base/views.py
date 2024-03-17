from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room ridwan'},
    {'id': 2, 'name': 'Room hafidhah'},
    {'id': 3, 'name': 'Room afkariana'},
]

def home(request):
    # return HttpResponse("ridwaanhall")
    # context = {'rooms': rooms}
    return render(request, 'base/home.html')

def room(request, pk):
    # return HttpResponse("room ridwaanhall")
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

def cek_doang(request):
    return render(request, 'main.html')
