import requests
from django.shortcuts import render


def level1(request):
    url = 'http://127.0.0.1:8000/api/level-api/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level1.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def level2(request, area_code_lv2):
    url = f'http://127.0.0.1:8000/api/level-api/{area_code_lv2}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level2.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def level3(request, area_code_lv2, area_code_lv3):
    url = f'http://127.0.0.1:8000/api/level-api/{area_code_lv2}/{area_code_lv3}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level3.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def level4(request, area_code_lv2, area_code_lv3, area_code_lv4):
    url = f'http://127.0.0.1:8000/api/level-api/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level4.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def level5(request, area_code_lv2, area_code_lv3, area_code_lv4, area_code_lv5):
    url = f'http://127.0.0.1:8000/api/level-api/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level5.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def cek_doang(request):
    pass
