from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import NewUser
from auction.models import Product
from django.core.paginator import Paginator
from datetime import datetime


# Create your views here.

def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

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
    return redirect('login')


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
