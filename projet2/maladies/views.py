from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib
def index(request):
    donnees={
        'nom':'charmante',
        'postnom':'lwanzo'
        
    }
    template=loader.get_template('index.html')
    return HttpResponse(template.render(donnees,request))

def maladie(request):

    template=loader.get_template('ml.html')
    return HttpResponse(template.render({},request))

def resultat(request):
    template=loader.get_template('ml.html')
    return HttpResponse(template.render({},request))

def predire(request):
    if request.method=="POST":

        toilettes=int(request.POST['toilettes'])
        mousticaire=int(request.POST['mousticaire'])
        douche=int(request.POST['douche'])
        poubelle=int(request.POST['poubelle'])
        genre=int(request.POST['genre'])
        age=int(request.POST['age'])
        tableau=[[toilettes,mousticaire,douche,poubelle,genre,age]]
        print(tableau)

        regression= joblib.load('charmante_tp_v1.pkl')
        resultat=regression.predict(tableau)
        print(resultat)
        
    return HttpResponse('ok')       