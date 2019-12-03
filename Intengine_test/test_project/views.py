from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'Intengine_test/login.html')
