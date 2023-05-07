from django.urls import path,include
from .views import sample1,sports,race,register,login,casino,cricket,football,basketball,icehockey,f1,bike,horse,start,about

urlpatterns = [
    path('home',sample1,name='NR'),
    path('sports',sports,name='SP'),
    path('race',race,name='RC'),
    path('casino',casino,name='CS'),
    path('register',register,name='RG'),
    path('/login',login,name='L'),
    path('cricket',cricket,name='CR'),
    path('football',football,name='FB'),
    path('basketball',basketball,name='BB'),
    path('icehockey',icehockey,name='IH'),
    path('f1',f1,name='F1'),
    path('bike',bike,name='B'),
    path('horse',horse,name='HR'),
    path('',start,name='s'),
    path('about',about,name='a'),
]