from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from user.models import Userinfo
import hashlib


class RegisterView(View):
    '''注册功能类视图'''
    def get(self,request):
        return render(request,'user/register.html')
    def post(self,request):
        uname_post = request.POST['uname']
        upwd_post = request.POST["upwd"]
        #对upwd加密．．．　　省略
        try:
            Userinfo.objects.create(uname=uname_post,upwd=upwd_post)
            return HttpResponse("OKKKKKK")
        except:
            return HttpResponse("error")


class LoginView(View):
    '''登录功能类视图'''
    def get(self,request):
        return render(request,'user/login.html')
    def post(self,request):
        uname_post = request.POST['uname']
        upwd_post = request.POST["upwd"]

        return HttpResponse("OK")