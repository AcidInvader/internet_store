from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory

# Create your views here.

def index(request):
    products = Product.objects.all()
    
    return render(request, 'mainapp/index-3.html', context={
        'products': products,
    })

def shop(request):
    title = 'Магазин'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    
    return render(request, 'mainapp/shop.html', context={
            'title': title,
            'categories': categories,
            'products': products,
        })

def category(request, pk):
    title = 'Магазин'
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, id=pk)
    products = Product.objects.filter(category=category)
    
    return render(request, 'mainapp/shop.html', context={
            'title': title,
            'categories': categories,
            'products': products,
        })

def about(request):
    return render(request, 'mainapp/about.html')

def product(request, pk=None):
    print(pk)

    title = "Продукты"
    link_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        return render(request, 'mainapp/product.html', context={
            'title': title,
            'link_menu': link_menu,
            'category': category,
            'products': products,
        })
    
    same_products = Product.objects.all()[3:5]
    return render(request, 'mainapp/product.html', context={
        'title': title,
        'link_menu': link_menu,
        'same_products': same_products,
    })

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
