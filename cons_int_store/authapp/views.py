from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'Вход'

    # Получаем форму на базе модели ShopUser
    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        # Получаем из словоря данных POST логин и пароль (не совсем словарь)
        # так как есть дополни-е методы 
        username = request.POST['username']
        password = request.POST['password']

        # Встроенный в Django аутентификатор
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            # Записывает пользователя в request
            # Залогинились
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    return render(request, 'authapp/login.html', context={
        'title': title,
        'login_form': login_form,
    })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

def edit(request):
    return HttpResponseRedirect(reverse, 'main')

def register(request):
    title = 'Регистрация'

    if request.method == 'POST':

        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        """
        request.FILES необходим, чтобы работала загрузка медиафайлов с формы — это словарь, содержащий
        информацию о переданных файлах. необходимо еще прописать атрибут
        enctype="multipart/form-data" для формы регистрации в теге <form>:
        """ 
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    return render(request, 'authapp/register.html', context={
        "title": title,
        "register_form": register_form,
    })
