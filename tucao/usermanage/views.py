from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
    return HttpResponse('hello')

def regist(request):
    if request.method == 'POST':
        try:
            user=User.objects.get(name=request.POST.get('name'))
            return HttpResponse('Exist')
        except Exception:
            name=request.POST.get('name')
            password=request.POST.get('password')
            gender=request.POST.get('gender',True)
            telnumber=request.POST.get('telnumber')

            user=User(name=name,password=password,gender=gender,telnumber=telnumber,exp='0',rank='1')
            user.save()
            return HttpResponse('Success')
    else:
        return HttpResponse('Error')

def login(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user
        try:
            user=User.objects.get(name=name)
        except:
            pass
        if user is not None:
            if password==user.password:
                request.session['user']=user.name
                return HttpResponse('Success')
            else:
                return HttpResponse('Password incorrot')
        else:
            return HttpResponse('user not eixist')
    else:
        return HttpResponse('Error')
