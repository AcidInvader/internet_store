from django.shortcuts import render
from mainapp.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()[:2]
    
    return render(request, 'mainapp/index-3.html', context={
        'products': products,
    })

def shop(request):
    return render(request, 'mainapp/shop.html')

def about(request):
    return render(request, 'mainapp/about.html')

def product(request, pk=None):
    print(pk)
    return render(request, 'mainapp/product.html')

def compare(request):
    return render(request, 'mainapp/compare.html')

def cart(request):
    return render(request, 'mainapp/cart.html')

def checkout(request):
    return render(request, 'mainapp/checkout.html')

def wishlist(request):
    return render(request, 'mainapp/wishlist.html')

def blog(request):
    return render(request, 'mainapp/blog.html')

def blog_details(request):
    return render(request, 'mainapp/blog-details.html')

def contact(request):
    return render(request, 'mainapp/contact.html')
