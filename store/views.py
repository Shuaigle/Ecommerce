from django.shortcuts import render

# Create your views here.
from .models import Category, Product

def all_products(request):
    # This is a query -> from Product select all
    products = Product.objects.all()
    # in Django, render use for loading templates, prepare data to send back to user
    return render(request, 'store/home.html', {'products': products})