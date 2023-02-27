from django.shortcuts import render


def login(request):
    return render(request, 'authapp/login.html')

def logout(request):
    return render(request, 'i told you not yet')

