from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user =auth.authenticate(username=uname,password=pwd)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mailid = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['cpassword']
        if pwd == cpwd :
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Already existing username")
                return redirect('registerapp:register')
            elif User.objects.filter(email=mailid).exists():
                messages.info(request,"Already existing Mailid")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=mailid,password=pwd)
                user.save();
                messages.info(request,"user created")
                return redirect('registerapp:login')
        else:
            messages.info(request,"Password missmatch")
        return redirect('/')
    return render(request, "register.html")



