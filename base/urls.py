from django.urls import path
from . import views

urlpatterns = [
    # make / redirect to level
    path('', views.level1, name='level1'),
    path('area', views.level1, name='level1'),
    path('area/<str:area_code_lv2>/', views.level2, name='level2'),
    # path('test', views.cek_doang, name='home')
]