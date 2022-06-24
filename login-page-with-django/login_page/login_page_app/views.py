from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

def homepage(request):
    return render(request,'home.html')

def registerpage(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request,'register.html',{'form':form})

def loginpage(request):
    return render(request, 'login.html')

# Create your views here.
