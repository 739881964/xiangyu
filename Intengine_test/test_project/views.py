from django.shortcuts import render, redirect, HttpResponse
import requests


# 登录验证
def login(request):
    if request.method == 'GET':
        return render(request, 'Intengine_test/login.html')
    if request.method == 'POST':
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        if (name == "xiangyu") and (pwd == "xiangyu123"):
            return redirect('Intengine_test/home.html')
        else:
            return HttpResponse("用户名或者密码错误")


# 首页
def home(request):
    # if submit(request):
    return render(request, 'Intengine_test/home.html')
