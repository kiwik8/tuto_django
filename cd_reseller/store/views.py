from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking, Variety, Price, Contact
from django.template import loader

# Create your views here.

def index(request):
    varieties = Variety.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_varieties = ["<li>{}</li>".format(variety.title) for variety in varieties]
    message = """<ul>{}</ul>""".format("\n".join(formatted_varieties))
    template = loader.get_template('store/index.html')
    return HttpResponse(template.render(request=request))

def listing(request):
    varieties = Variety.objects.filter(available=True)
    formatted_varieties = ["<li>{}</li>".format(variety.title) for variety in varieties]
    message = """<ul>{}</ul>""".format("\n".join(formatted_varieties))
    return HttpResponse(message)


def detail(request, variety_id):
    variety = Variety.objects.get(pk=variety_id)
    prices = " ".join([str(price.value) for price in variety.prices.all()])
    message = f"La variété est {variety.title}, et son prix est de {prices}$"
    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')
    if not query:
        varieties = Variety.objects.all()
    else:
        varieties = Variety.objects.filter(title__icontains=query)
    if not varieties.exists():
        varieties = Variety.objects.filter(prices__value__icontains=query)

    if not varieties.exists():
        message = "Roh je ne trouve rien ! "

    else:
        varieties = ["<li>{}</li>".format(variety.title) for variety in varieties]
        message = """
            Nous avons trouvé les variétés correspondant à votre requête ! Les voici :
            <ul>{}</ul>
        """.format(" ".join(varieties))

    
    return HttpResponse(message)