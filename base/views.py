import requests
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room ridwan'},
    {'id': 2, 'name': 'Room hafidhah'},
    {'id': 3, 'name': 'Room afkariana'},
]

# def home(request):
#     # return HttpResponse("ridwaanhall")
#     # context = {'rooms': rooms}
#     return render(request, 'base/home.html')

def home(request):
    url = 'http://127.0.0.1:8000/api/votes/'
    response = requests.get(url)
    
    if response.status_code == 200:
        # Assuming the JSON response contains the data you want to pass to the template
        context = response.json()
        
        total_votes = context['chart']['100025'] + context['chart']['100026'] + context['chart']['100027']
        
        context['total_votes'] = total_votes
        
        return render(request, 'base/home.html', context)
    else:
        # Handle the case when the request fails
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def room(request, pk):
    # return HttpResponse("room ridwaanhall")
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

def cek_doang(request):
    url_names = "http://127.0.0.1:8000/api/names/"
    url = 'http://127.0.0.1:8000/api/votes/'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # Assuming the JSON response contains the data you want to pass to the template
        context = response.json()
        
        total_votes = context['chart']['100025'] + context['chart']['100026'] + context['chart']['100027']

        context['total_votes'] = total_votes

        return render(request, 'base/home.html', context)
    else:
        # Handle the case when the request fails
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})
    # return render(request, 'base/home.html')
