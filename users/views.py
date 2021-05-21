from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import NewUser
from auction.models import Product, Bid
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Sum, Count
from django.http import JsonResponse


# Create your views here.

def Index(request):
    return render(request, 'indexmain.html')


def AdminLogin(request):
    if request.user.is_authenticated:
        return redirect('admin-dashboard')

    if request.method == 'POST':
        admin = NewUser.objects.values('email').filter(user_name='admin')
        email_list = []
        for i in admin:
            email_list.append(i['email'])

        email_str = ''.join(email_list)
        first, second = email_str.split('@')

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = username + '@' + second

        adm = authenticate(request, email=email, password=password)
        if adm is not None:
            login(request, adm)
            return redirect('admin-dashboard')

    return render(request, 'adminLogin.html')


def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard', request.user)

    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard', user)
            else:
                messages.error(request, 'Username or Password is Invalid!!!')

            if not user:
                nemail = request.POST.get('email')
                npassword = request.POST.get('password')

                username = str(nemail.split('@')[0])
                NewUser.objects.create_user(email=nemail, user_name=username, first_name=username, password=npassword)

                new_user = authenticate(request, email=nemail, password=npassword)

                if new_user is not None:
                    login(request, new_user)
                    return redirect('dashboard', new_user)

    return render(request, 'index.html')


@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def Dashboard(request, user):
    name = NewUser.objects.get(user_name=user)
    product = Product.objects.all()
    paginator = Paginator(product, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'name': name,
        'products': product,
        'page_obj': page_obj,
        'today': datetime.now()
    }

    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def AdminDashboard(request):
    running = Product.objects.filter(end_date__gte=datetime.today())
    value = Product.objects.filter(end_date__gte=datetime.today()).aggregate(Sum('min_price'))

    # product_added_count = Product.objects.all().count()

    created_product = []
    completed_auction = []
    labels = []
    total_value = []

    for i in range(1, 31):
        data_count = Product.objects.filter(created__day=i).count()
        completed = Product.objects.filter(created__day=i).filter(end_date__lt=datetime.today()).count()
        sum_value = Bid.objects.filter(date__day=i).aggregate(Sum('price'))
        # sum_value = JsonResponse(sum_value, safe=False)
        total_value.append(sum_value)
        completed_auction.append(completed)
        created_product.append(data_count)

        labels.append(i)

    print(list(total_value))
    tv = []
    for i in total_value:
        tv.append(i['price__sum'])

    tvs = [0 if i == None else i for i in tv]

    context = {
        'running': running,
        'value': value,
        'created_product': created_product,
        'completed_auction': completed_auction,
        'total_value': tvs,
        'label': labels
    }
    return render(request, 'adminDashboard.html', context)


def Chart(request):
    product_added_count = Product.objects.annotate(Count('created'))

    data = []
    labels = []

    for i in product_added_count:
        data.append(i['created'])
        labels.append(datetime.strftime(i.created, '%/%d'))

    return JsonResponse({
        'data': data,
        'labels': labels
    })
