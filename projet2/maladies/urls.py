from django.urls import path
from. import views


urlpatterns=[

    path('',views.index,name="index"),
    path('maladie/',views.maladie, name='maladie'),
    path('predict/',views.predire,name='predire'),
    path('resultat/',views.resultat,name='resultat')

    
]