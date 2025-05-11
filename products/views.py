from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request, 'index.html')

def products_list(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    product_list = Product.objects.all()
    product_paginator = Paginator(product_list, 9)
    product_list = product_paginator.get_page(page)
    context = {
        'products': product_list
    }
    return render(request, 'products.html', context)

def product_details(request):
    return render(request, 'products_detail.html')