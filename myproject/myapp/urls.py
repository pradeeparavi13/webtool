from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu1/', views.menu1, name='menu1'),
    path('menu2/', views.menu2, name='menu2'),
    path('menu3/', views.menu3, name='menu3'),
    path('menu4/', views.menu4, name='menu4'),
    path('menu5/', views.menu5, name='menu5'),
]