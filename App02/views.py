from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return HttpResponse('Hello World!')


def handle_example(request):
    return render(request, 'app02/index.html')


def load_template(request):
    # # 加载末班文件，生成渲染对象
    # obj = loader.get_template('example.html')
    # # print(obj, type(obj))
    # context = {'name': 'Tom'}
    # res = obj.render(context)
    # # 渲染的结果生成html字符串
    # print(res)
    # return HttpResponse(res)

    # render一次加载和渲染一起进行，是一种快捷方式
    res = render(request, 'example.html', {'name': 'ALIS'})
    return HttpResponse(res)


def handle_var(request):
    num = 12
    name = '伟大的意大利左后卫'
    students = [12, 14, 56, 78, 12]
    student = {'name': "马儿蒂尼", 'age': 23}
    return render(request, 'var.html', locals())


def handle_filter(request):
    num = 12
    name = '伟大的意大利左后卫'
    age = None
    t1 = datetime.now()
    return render(request, '过滤器.html', locals())
