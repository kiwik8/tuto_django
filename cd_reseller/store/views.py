from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Booking, Variety, Price, Contact
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ContactForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    varieties = Variety.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'varieties' : varieties
    }
    return render(request, 'store/index.html', context)

def listing(request):
    varieties_list = get_list_or_404(Variety, available=True)
    paginator = Paginator(varieties_list, 6)
    page = request.GET.get('page')
    try:
        varieties = paginator.page(page)
    except PageNotAnInteger:
        varieties = paginator.page(1)
    except EmptyPage:
        varieties = paginator.page(paginator.num_pages)
    context = {
        'varieties' : varieties,
        'paginate' : True
    }
    return render(request, 'store/listing.html', context)


def detail(request, variety_id):
    variety = get_object_or_404(Variety, pk=variety_id)
    prices = " ".join([str(price.value) for price in variety.prices.all()])
    context = {
        'variety_title' : variety.title,
        'prices_value' : prices,
        'variety_id' : variety_id,
        'thumbnail' : variety.picture,
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            try:
                contact = Contact.objects.get(email=email)
            except ObjectDoesNotExist:
                contact = Contact.objects.create(
                    email=email,
                    name=name
                )

            variety = get_object_or_404(Variety, pk=variety_id)
            booking = Booking.objects.create(
                variety=variety,
                contact=contact
            )
            variety.available = False
            variety.save()
            context = {
                'variety_title' : variety.title,
                'variety_picture' : variety.picture
            }

            return render(request, 'store/merci.html', context)
        else:
            form['errors'] = form.errors.items()
    else:
        form = ContactForm
        


    context['form'] = form
    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        varieties = Variety.objects.all()
    else:
        varieties = Variety.objects.filter(title__icontains=query)
  
    title = "Results from your request %s"%query
    context = {
        'varieties' : varieties,
        'title' : title
    }
    return render(request, 'store/search.html', context)