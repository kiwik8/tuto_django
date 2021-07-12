from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking, Variety, Price, Contact
from django.template import loader

# Create your views here.

def index(request):
    varieties = Variety.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'varieties' : varieties
    }
    return render(request, 'store/index.html', context)

def listing(request):
    varieties = Variety.objects.filter(available=True)
    context = {
        'varieties' : varieties
    }
    return render(request, 'store/listing.html', context)


def detail(request, variety_id):
    variety = Variety.objects.get(pk=variety_id)
    prices = " ".join([str(price.value) for price in variety.prices.all()])
    prices_value = " ".join(prices)
    context = {
        'variety_title' : variety.title,
        'prices_value' : prices_value,
        'variety_id' : variety_id,
        'thumbnail' : variety.picture
    }
    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        varieties = Variety.objects.all()
    else:
        varieties = Variety.objects.filter(title__icontains=query)
    if not varieties.exists():
        varieties = Variety.objects.filter(prices__value__icontains=query)
  
    title = "Résultats pour votre requête %s"%query
    context = {
        'varieties' : varieties,
        'title' : title
    }
    return render(request, 'store/search.html', context)