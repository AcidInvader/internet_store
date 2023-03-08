"""cons_int_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('', mainapp.index, name='main'),
    path('shop/', mainapp.shop, name='shop'),
    path('about/', mainapp.about, name='about'),
    path('product/', include('mainapp.urls', namespace='product')),
    path('compare/', mainapp.compare, name='compare'),
    path('cart/', mainapp.cart, name='cart'),
    path('checkout/', mainapp.checkout, name='checkout'),
    path('wishlist/', mainapp.wishlist, name='wishlist'),
    path('blog/', mainapp.blog, name='blog'),
    path('blog-details/', mainapp.blog_details, name='blog-details'),
    path('contact/', mainapp.contact, name='contact'),
]

# Чтобы Django раздавал медиафайлы на этапе разработки, необходимо 
# сообщить Django, что нужно папку на диске MEDIA_ROOT сделать доступной по
# сетевому адресу MEDIA_URL.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)