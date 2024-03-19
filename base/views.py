import requests
from django.shortcuts import render


def home(request):
    url = 'http://127.0.0.1:8000/api/home-api/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/home.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def cek_doang(request):
    pass
