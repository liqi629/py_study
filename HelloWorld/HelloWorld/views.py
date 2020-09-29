from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")
# def runoob(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)

# def runoob(request):
#   views_name_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
#   return  render(request,"runoob.html", {"views_name_list":views_name_list})


def runoob(request):
    name = request.POST.get("name")
    return HttpResponse('姓名：{}'.format(name))