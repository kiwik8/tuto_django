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