from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    # This is a query -> from Product select all
    products = Product.objects.all()
    # in Django, render use for loading templates, prepare data to send back to user
    return render(request, 'store/home.html', {'products': products})

# urls -> views -> models
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'products': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
