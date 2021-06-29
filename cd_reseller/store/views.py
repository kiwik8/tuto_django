from django.shortcuts import render
from django.http import HttpResponse
from .models import VARIETIES
# Create your views here.

def index(request):
    return HttpResponse("Yo les gens !")


def listing(request):
    variety = ["<li>{}</li>".format(variety['name']) for variety in VARIETIES]
    message = """<ul>{}</ul>""".format("\n".join(variety))
    return HttpResponse(message)


def detail(request, variety_id):
    id = int(variety_id)
    variety = VARIETIES[id]
    price = " ".join([price['price'] for price in variety['prices']])
    message = "The variety is {} and it price is {}$".format(variety['name'], price)
    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Tu ne me demandes rien!"
    else:
        varieties = [
            variety for variety in VARIETIES
            if query in variety['name']
        ]
        if len(varieties) == 0:
            message = "Nop j'ai rien trouvé!"

        else:
            varieties = ["<li>{}</li>".format(variety['name']) for variety in varieties]
            message = """
                Nous avons trouvé les variétés correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(varieties))

    
    return HttpResponse(message)