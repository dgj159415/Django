#from django.contrib.auth import authenticate
import datetime
from time import sleep

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.core import serializers
import json

from web.models import UserInfo

#初始化方法
def init(request):
    sleep(0.8)
    #name = request.COOKIES.get('username')
    name = request.session.get('username', default=None)
    if name==None:
        return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/index/')


#注册发放
def register(request):
    return render(request, 'register.html')
#登录成功后设置cooike
# def setcooike(request):
#     if request.method == 'GET':
#         data = request.GET
#         username = data.get("username")
#         response = HttpResponse(username)
#         response.set_cookie('username', username, max_age=3600)#一个小时
#         return response
#跳转主页操作
def index(request):
    sleep(0.8)
    name=request.session.get('username', default=None)
    #= request.COOKIES.get('username')
    if name == None:
        return render(request, 'login.html')
    else:
        context={}
        context['username']=name
        return render(request, 'index.html',context)
# #删除cooike
# def delecooike(request):
#     # data = request.GET
#     # username = data.get("username")
#     response = HttpResponse('删除cooike')
#     response.delete_cookie("username")
#     return response
#退出操作
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        dict = {
            "result": 0,
            "msg": "退出登录！"
        }
        try:
            del request.session['username']
        except KeyError:
            pass
        return JsonResponse(dict, safe=False)
#登录操作
def login(request):
    # try:
    #     name = request.COOKIES['name']
    #     return HttpResponseRedirect('/index/')
    # except:
    if request.method == 'POST':
        dict={}
        data=request.POST
        username=data.get("username")
        password=data.get("password")
        try:
            response = UserInfo.objects.get(username=username)
        except:
            dict={
                    "result":2,
                    "msg":"用户名不存在！"
                }
            return JsonResponse(dict, safe=False)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            dict={
                "result":0,
                "msg":"登录成功！"
            }
            request.session['username'] = username
            return JsonResponse(dict,safe=False)
        else:
            dict = {
                "result": 1,
                "msg": "密码错误！"
            }
            return JsonResponse(dict,safe=False)
def register_submit(request):
    if request.method=='POST':
        context={}
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username=username, password=password,email=email)

        aaa=UserInfo.objects.count()

        UserInfo.objects.create(username=username,email=email,id=int(aaa)+1)
        auth.login(request, user)
        dict = {
            "result": 0,
            "msg": "注册成功！"
        }
        request.session['username'] = username
        return JsonResponse(dict, safe=False)

def setpassword(request):
    if request.method=='POST':
        context={}
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username=username, password=password,email=email)

        aaa=UserInfo.objects.count()

        UserInfo.objects.create(username=username,email=email,id=int(aaa)+1)
        auth.login(request, user)
        dict = {
            "result": 0,
            "msg": "注册成功！"
        }
        request.session['username'] = username
        return JsonResponse(dict, safe=False)
def select(request):
    response = UserInfo.objects.get(username='dugaojian')
    return HttpResponse(response.email)
    # data={}
    # s = User.objects.all()
    # data['result']=json.loads(serializers.serialize('json',s))
    # return JsonResponse(data)
def test(request):
    response = HttpResponse("这是我的cookie")
    response.set_cookie('name', 'dugaojian', max_age=200)
    return response
    # data = {}
    # s = User.objects.all()
    # data['result'] = json.loads(serializers.serialize('json', s))
    # return JsonResponse(data)





