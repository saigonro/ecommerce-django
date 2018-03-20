from django.shortcuts import render
from .models import Product

def get_products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})
