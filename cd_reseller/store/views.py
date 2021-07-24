from django.shortcuts import render, get_object_or_404
from .models import Booking, Variety, Contact
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ContactForm, VarietyForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def index(request):
    varieties = Variety.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'varieties': varieties
    }
    return render(request, 'store/index.html', context)

def listing(request):
    varieties_list = Variety.objects.filter(available=True)
    paginator = Paginator(varieties_list, 6)
    page = request.GET.get('page')
    try:
        varieties = paginator.page(page)
    except PageNotAnInteger:
        varieties = paginator.page(1)
    except EmptyPage:
        varieties = paginator.page(paginator.num_pages)
    context = {
        'varieties': varieties,
        'paginate': True
    }
    return render(request, 'store/listing.html', context)


def detail(request, variety_id):
    variety = get_object_or_404(Variety, pk=variety_id)
    context = {
        'variety_title': variety.title,
        'variety_price': variety.price,
        'variety_id': variety_id,
        'thumbnail': variety.picture,
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
            variety.stock = variety.stock - 1
            if variety.stock == 0:
                variety.available = False
            variety.save()
            Booking.objects.create(
                variety=variety,
                contact=contact
            )
            context = {
                'variety_title': variety.title,
                'variety_picture': variety.picture
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

    title = "Results from your request %s" % query
    context = {
        'varieties': varieties,
        'title': title
    }
    return render(request, 'store/search.html', context)


def about(request):
    return render(request, 'store/about.html')


@user_passes_test(lambda u: u.is_superuser, login_url='/admin/login/?next=/manage/')
def manage_variety(request):
    context = {

    }
    if request.method == "POST":
        form = VarietyForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            picture = form.cleaned_data['picture']
            price = form.cleaned_data['price']
            stock = form.cleaned_data['stock']

            try:
                variety = Variety.objects.get(title=title)
            except ObjectDoesNotExist:
                variety = None

            if not variety:
                variety = Variety.objects.create(
                    title=title,
                    picture=picture,
                    price=price,
                    stock=stock
                )
            else:
                context['message'] = "Variety already exists"
                return render(request, 'store/created.html', context)

            context = {
                'variety_title': variety.title,
                'variety_picture': variety.picture,
                'variety_price': variety.price,
                'variety_stock': variety.stock,
                'message': 'Variety successfully added!',
                'success': True
            }

            return render(request, 'store/created.html', context)
        else:
            form['errors'] = form.errors.items()
    else:
        form = VarietyForm
    context['form'] = form
    return render(request, 'store/manage.html', context)
