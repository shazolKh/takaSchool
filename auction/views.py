from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

@login_required(login_url='login')
def AddProduct(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user.pk
        name = data.get('name')
        min_price = data.get('price')
        end_date = data.get('e_date')
        description = data.get('description')
        image = request.FILES.get('image')

        product = Product(user_id=user, name=name, min_price=min_price, end_date=end_date,
                          description=description, image=image)
        product.save()
        return redirect('dashboard', request.user)

    return render(request, 'addProduct.html')


@login_required(login_url='login')
def MyPostedItems(request, pk):
    products = Product.objects.filter(user_id=pk)

    paginator = Paginator(products, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'page_obj': page_obj,
    }
    return render(request, 'myPostedItems.html', context)

