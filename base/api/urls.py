from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    
    path('names/', views.Names.as_view(), name='names'),
    
    path('sengketa/', views.Sengketa.as_view(), name='sengketa_api'),

    path('wilayah/<str:wilayah_tingkat2>/', views.WilayahAPIView.as_view(), name='wilayah_tingkat_2'),
    path('wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>/', views.WilayahAPIView.as_view(), name='wilayah_tingkat_3'),
    path('wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>/<str:wilayah_tingkat4>/', views.WilayahAPIView.as_view(), name='wilayah_tingkat_4'),
    path('wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>/<str:wilayah_tingkat4>/<str:wilayah_tingkat5>/', views.WilayahAPIView.as_view(), name='wilayah_tingkat_5'),

    path('votes/', views.VotesAPIView.as_view(), name='votes_tingkat_1'),
    path('votes/<str:votes_tingkat2>/', views.VotesAPIView.as_view(), name='votes_tingkat_2'),
    path('votes/<str:votes_tingkat2>/<str:votes_tingkat3>/', views.VotesAPIView.as_view(), name='votes_tingkat_3'),
    path('votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>/', views.VotesAPIView.as_view(), name='votes_tingkat_4'),
    path('votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>/<str:votes_tingkat5>/', views.VotesAPIView.as_view(), name='votes_tingkat_5'),
    path('votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>/<str:votes_tingkat5>/<str:votes_tingkat6>/', views.VotesAPIView.as_view(), name='votes_tingkat_6'),
    
    path('level-api/', views.Level1API.as_view(), name='level_api_1'),
    path('level-api/<str:area_code_lv2>/', views.Level2API.as_view(), name='level_api_2'),
    path('level-api/<str:area_code_lv2>/<str:area_code_lv3>/', views.Level3API.as_view(), name='level_api_3'),
    path('level-api/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/', views.Level4API.as_view(), name='level_api_4'),
    path('level-api/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/<str:area_code_lv5>/', views.Level5API.as_view(), name='level_api_5'),
    path('level-api/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/<str:area_code_lv5>/<str:area_code_lv6>/', views.Level6API.as_view(), name='level_api_6'),

    path('rekap/', views.HasilRekap.as_view(), name='rekap_1'),
    path('rekap/<str:area_code_lv2>/', views.HasilRekap.as_view(), name='rekap_2'),
    path('rekap/<str:area_code_lv2>/<str:area_code_lv3>/', views.HasilRekap.as_view(), name='rekap_3'),
    path('rekap/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/', views.HasilRekap.as_view(), name='rekap_4'),
    path('rekap/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/<str:area_code_lv5>/', views.HasilRekap.as_view(), name='rekap_5'),

    path('rekap-api/', views.HasilRekap1API.as_view(), name='rekap_api_1'),
    path('rekap-api/<str:area_code_lv2>/', views.HasilRekap2API.as_view(), name='rekap_api_2'),
    path('rekap-api/<str:area_code_lv2>/<str:area_code_lv3>/', views.HasilRekap3API.as_view(), name='rekap_api_3'),
    path('rekap-api/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/', views.HasilRekap4API.as_view(), name='rekap_api_4'),
    path('rekap-api/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/<str:area_code_lv5>/', views.HasilRekap5API.as_view(), name='rekap_api_5'),
]