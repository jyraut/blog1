from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import *
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_http_methods
# from myapp.forms import *
# Create your views here.


def index(request):
    data=Post.objects.all()
    return render(request,'index.html',{'data':data})
    
    
    

def user_login(request):
    return render(request,'login.html')





@require_http_methods(["POST"])
def user_auth(request):
    # if request.method=='POST':
        u= request.POST.get('username')
        p= request.POST.get('password')

        user = authenticate(username=u,password=p)

        if user is not None:
            login(request,user)
            return redirect('login')
        else:
            return HttpResponse('invalid username or password')

def home(request):
    if request.user.is_authenticated:
        return index(request)
    else:
        return user_login(request)


def detail_post(request,d):
    z = Post.objects.get(id=d)
    return render(request,'detail.html',{'z':z})

def delete(request,d):
    z = Post.objects.get(id=d)
    z.delete()
    return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')


def add_post(request):   
    if request.method=='POST':
        form =Post_form(request.POST)
        if form.is_valid():
            f1 = form.save(commit=False)
            f1.user = request.user
            f1.save()
            return redirect('login')

    else:
        form = Post_form()
        #data = Post.objects.all()
    return render(request,'post.html',{'form':form})

# def user_reg(request):
#     if request.method == 'POST':
#         form = reg_form(request.POST)
#         if form.is_valid():
#             d=form.cleaned_data
#             u = d['username']
#             e = d['email']
#             p = d['password']
#             User.objects.create_user(username=u,email=e,password=p)
#             return redirect('login')
#     else:
#         form = reg_form()
#     return render(request,'reg.html',{'form':form})
# Create your views here.

def user_reg(request):
    if request.method=='POST':
        regform=reg_form(request.POST)
        profile_form=profileform(request.POST,request.FILES)

        if regform.is_valid() and profile_form.is_valid():
            username = regform.cleaned_data.get('username')
            email = regform.cleaned_data.get('email')
            password =regform.cleaned_data.get('password')

            User.objects.create_user(username=username,password=password,email=email)

            u= User.objects.get(username=username)
            f= profile_form.save(commit=False)
            f.user_profile=u
            f.save()
            return HttpResponseRedirect('/')
    else:
        regform=reg_form()
        profile_form=profileform()
    return render(request,'home.html',{'regform':regform,'profile_form':profile_form})