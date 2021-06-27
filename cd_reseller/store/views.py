from django.shortcuts import render
from django.http import HttpResponse
from .models import VARIETIES
# Create your views here.

def index(request):
    return HttpResponse("Yo les gens !")


def listing(request):
    variety = ["<li>{}</li>".format(item['name']) for item in VARIETIES.values()]
    message = """<ul>{}</ul>""".format("\n".join(variety))
    return HttpResponse(message)