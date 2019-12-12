from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def account(request):
    return render(request, 'count/home.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'count/log_in.html', {'error': 'Username or Password is incorrect.'})
    else:
        return render(request, 'count/log_in.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'count/sign_up.html',{'error':'Username has already been taken'})
        #User has info and wants an account
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'count/sign_up.html', {'error': 'Passwords must match'})

    else:
        #User wants to enter info
        return render(request, 'count/sign_up.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')