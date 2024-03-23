from django.urls import path
from . import views

urlpatterns = [
    # make / redirect to level
    path('', views.level1, name='home'),
    path('hitung-suara/', views.level1, name='level1'),
    path('hitung-suara/<str:area_code_lv2>/', views.level2, name='level2'),
    path('hitung-suara/<str:area_code_lv2>/<str:area_code_lv3>/', views.level3, name='level3'),
    path('hitung-suara/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/', views.level4, name='level4'),
    path('hitung-suara/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/<str:area_code_lv5>/', views.level5, name='level5'),
    path('hitung-suara/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/<str:area_code_lv5>/<str:area_code_lv6>/', views.level6, name='level6'),
    path('sengketa/', views.sengketa, name='sengketa'),
    path('rekapitulasi/', views.rekap_hasil1, name='rekapitulasi1'),
    path('rekapitulasi/<str:area_code_lv2>/', views.rekap_hasil2, name='rekapitulasi2'),
]