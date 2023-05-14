from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from mainapp.models import Product
from .models import Basket


# Create your views here.
def view(request):
    basket = Basket.objects.filter(user=request.user)
    return render(request, 'basketapp/wishlist.html', context={
        'basket': basket,
    })

def add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    basket_item = Basket.objects.filter(user=request.user, product=product)

    if basket_item: 
        # if basket has anything we take first item
        basket = basket_item.first()
    else:
        basket = Basket(user=request.user, product=product)

    # we incrise value of items
    basket.quantity += 1
    basket.save()

    # from request.META.get('HTTP_REFERER') we can get previous adderes of user
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove(request, basket_item_id):
    basket = get_object_or_404(Basket, pk=basket_item_id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))