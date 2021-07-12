from django.shortcuts import render, get_object_or_404, get_list_or_404
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
    varieties = get_list_or_404(Variety, available=True)
    context = {
        'varieties' : varieties
    }
    return render(request, 'store/listing.html', context)


def detail(request, variety_id):
    variety = get_object_or_404(Variety, pk=variety_id)
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
        varieties = get_list_or_404(Variety)
    else:
        varieties = get_list_or_404(Variety, title__icontains=query)
  
    title = "Results from your request %s"%query
    context = {
        'varieties' : varieties,
        'title' : title
    }
    return render(request, 'store/search.html', context)