from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):

    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Youhave been login sucess fully")
            return redirect('home')
        else:
            messages.success(request,"login Error , Please try agin...")
            return redirect('home')
    else:
        return render(request, 'home.html',{'records' : records })

def logout_user(request):
    logout(request)
    messages.success(request,"You have been log out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Django's UserCreationForm uses 'password1' for the password field
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been successfully registered.")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html',{'form':form})
