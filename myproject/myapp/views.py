from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def menu1(request):
    return render(request, 'menu1.html')

def menu2(request):
    return render(request, 'menu2.html')

def menu3(request):
    return render(request, 'menu3.html')

def menu4(request):
    return render(request, 'menu4.html')

def menu5(request):
    return render(request, 'menu5.html')