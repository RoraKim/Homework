from email import message
import re
from django.shortcuts import render
from django.test import RequestFactory

# Create your views here.
def throw(request):
    #throw라는 html파일은 어디에 있느냐?
    #django 에서 모든 template은 각 app의 templates 폴더에 만든다. 
    return render(request, 'throw.html')


def catch(request):
    # print(dir(request))
    print('=' * 30)
    print(request.GET.get('message'))
    print('=' * 30)
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'catch.html', context)


def hello(request, name):
    cnontext = {
        'name' : name,
    }
    return render(request, 'hello.html')