from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    return render(request, 'Intengine_test/login.html')


# 点击确认按钮，跳转到首页
def do_login(request):
    return redirect(home_page)


# 首页
def home_page(request):
    # if submit(request):
    return render(request, 'Intengine_test/home.html')

