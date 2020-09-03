from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse


def tologin(request):
    return render(request, 'login.html')


def login(request):
    name = request.POST.get('name')

    response = redirect(reverse('cook:welcome'))
    response.set_cookie('name', name)

    return response


def welcome(request):
    name = request.COOKIES.get('name', '游客')

    context = {
        'name': name
    }
    return render(request, 'welcome.html', context=context)


def logout(request):
    response = render(request, 'welcome.html')
    response.delete_cookie('name')
    return response
