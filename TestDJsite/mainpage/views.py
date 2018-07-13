from django.shortcuts import render

def index(request):
    return render(request, 'mainpage/home.html')

def contact(request):
    return render(request, 'mainpage/basic.html', {'text':['first listt elem', 'second listt elem']})
