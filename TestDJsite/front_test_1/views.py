from django.shortcuts import render

def index(request):
    return render(request, 'front_test_1/test.html')
