from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('这里是用户的首页')


def show(request, name, age):
    return HttpResponse(name + ':' + str(age) + '岁')


def call(request, call):
    return render(request, 'call.html')


def req(request):
    # print(request.method)
    # print(request.GET.get('username'))  # username 不存在返回None
    # print(request.GET['username'])  # username 不存在会报错
    # print(request.GET.getlist('age'))
    # request.META.get('HTTP_REFERER')
    return HttpResponse('你是从这个地址跳到本页面的，修改了一下，试试git' + request.META.get('HTTP_REFERER'))