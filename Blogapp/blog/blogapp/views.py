from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import PostForm,SignUpForm, LogInForm
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib import messages
# Create your views here.
def home(request):
    post = Post.objects.filter(id=1)
    return render(request, "blogapp/home.html",{"post":post})


def AddPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                txt=form.cleaned_data["title"]
                con=form.cleaned_data["content"]
                author=form.cleaned_data["author"]
                
                data=Post(title=txt, content=con, author=author)
                form.save()
        else:
            form=PostForm()
        return render(request, "blogapp/addpost.html",{"form":form})
    else:
        return HttpResponseRedirect('/login/')

def Update(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            data=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
        else:
            data=Post.objects.get(pk=id)
            form=PostForm(instance=data)
        return render(request, "blogapp/updatepost.html",{"form":form})
    else:
        return HttpResponseRedirect('/login/')

def read(request,id):
    post=Post.objects.get(pk=id)
    return render(request, 'blogapp/post.html',{"post":post})

def Dele(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return HttpResponseRedirect("/home/")
        
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations your Account succesfully cereated...!!!")
            user=form.save()
            group = Group.objects.get(name='Authors')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blogapp/signup.html', {'form':form})


def log_in(request):
    if  not request.user.is_authenticated:
        if request.method=="POST":
            form = LogInForm(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                upass=form.cleaned_data["password"]
                user=authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Log In successfull...!!!")
                    return HttpResponseRedirect('/home/')
        else:
            form = LogInForm()
        return render(request, "blogapp/login.html",{"form":form})
    else:
        return HttpResponseRedirect('/home/')
        

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')
    
