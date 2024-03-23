import requests
from django.shortcuts import render
from base.api.Ridwaanhall import DATABASE_API

def level1(request):
    url = DATABASE_API + 'api/level-api/'
    response = requests.get(url)

    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level1.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def level2(request, area_code_lv2):
    url = DATABASE_API + f'api/level-api/{area_code_lv2}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level2.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def level3(request, area_code_lv2, area_code_lv3):
    url = DATABASE_API + f'api/level-api/{area_code_lv2}/{area_code_lv3}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level3.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def level4(request, area_code_lv2, area_code_lv3, area_code_lv4):
    url = DATABASE_API + f'api/level-api/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level4.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def level5(request, area_code_lv2, area_code_lv3, area_code_lv4, area_code_lv5):
    url = DATABASE_API + f'api/level-api/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level5.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})
    
    
def level6(request, area_code_lv2, area_code_lv3, area_code_lv4, area_code_lv5, area_code_lv6):
    url = DATABASE_API + f'api/level-api/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/{area_code_lv6}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/level6.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def sengketa(request):
    url = DATABASE_API + 'api/sengketa/'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        json_data = response.json()
        context = {'json_data': json_data}
        return render(request, 'base/sengketa.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def rekap_hasil1(request):
    url = DATABASE_API + 'api/rekap-api/'
    response = requests.get(url)
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/rekap_hasil1.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})
    
def rekap_hasil2(request, area_code_lv2):
    url = DATABASE_API + f'api/rekap-api/{area_code_lv2}/'
    response = requests.get(url)
    if response.status_code == 200:
        context = response.json()
        return render(request, 'base/rekap_hasil2.html', context)
    else:
        error_message = f"Failed to fetch data from {url}. Status code: {response.status_code}"
        return render(request, 'base/error.html', {'error_message': error_message})

def cek_doang(request):
    pass
