from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    
    path('names/', views.Names.as_view(), name='names'),
    
    path('sengketa/', views.Sengketa.as_view(), name='sengketa'),
    
    path('wilayah/<str:wilayah_tingkat2>/', views.WilayahTingkat2.as_view(), name='wilayah_tingkat_2'),
    path('wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>/', views.WilayahTingkat3.as_view(), name='wilayah_tingkat_3'),
    path('wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>/<str:wilayah_tingkat4>/', views.WilayahTingkat4.as_view(), name='wilayah_tingkat_4'),
    path('wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>/<str:wilayah_tingkat4>/<str:wilayah_tingkat5>/', views.WilayahTingkat5.as_view(), name='wilayah_tingkat_5'),

    path('votes/', views.VotesTingkat1.as_view(), name='votes_tingkat_1'),
    path('votes/<str:votes_tingkat2>/', views.VotesTingkat2.as_view(), name='votes_tingkat_2'),
    path('votes/<str:votes_tingkat2>/<str:votes_tingkat3>/', views.VotesTingkat3.as_view(), name='votes_tingkat_3'),
    path('votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>/', views.VotesTingkat4.as_view(), name='votes_tingkat_4'),
    path('votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>/<str:votes_tingkat5>/', views.VotesTingkat5.as_view(), name='votes_tingkat_5'),
    path('votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>/<str:votes_tingkat5>/<str:votes_tingkat6>/', views.VotesTingkat6.as_view(), name='votes_tingkat_6'),
    
    path('level-api/', views.Level1API.as_view(), name='level_api_1'),
    path('level-api/<str:area_code_lv2>/', views.Level2API.as_view(), name='level_api_2'),
]