from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def shop(request):
    return render(request, 'mainapp/shop.html')

def about(request):
    return render(request, 'mainapp/about.html')