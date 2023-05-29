from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Department, Doctors
from . import forms
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib.auth import User,auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse




# Create your views here.
def index(request):
    # return HttpResponse("Home Page")
    return render(request, "index.html")



def home(request):
    # return HttpResponse("Home Page")

    return render(request, "home.html")
def about(request):

    #return HttpResponse("About Page")


    return render(request, "about.html")
def base(request):
    return render(request, "base.html")
def booking(request):
    #form = forms.BookingForm()
    if request.method == "POST":
        formdemo= BookingForm(request.POST)
        if formdemo.is_valid():
            formdemo.save()
            return render(request,'c.html')
    myform1 = BookingForm()
    dict_book = {
        'formkey': myform1

    }
    return render(request, "booking.html",dict_book)
def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
      }
    return render(request, "doctors.html",dict_docs)
def contact(request):
    return render(request, "contact.html")
def department(request):
    dept_dict = {
        'dept': Department.objects.all()
    }
    return render(request, "department.html",dept_dict)
def career_view(request):
    form = forms.careerform()
    return render(request, "career.html",context={"form":form})
def regis(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username already exists')
                return HttpResponseRedirect(reverse('register'))
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.set_password(password)
                user.save()
                return redirect("login_user")
        else:
            messages.add_message(request, messages.ERROR, 'password not matching')
            return HttpResponseRedirect(reverse('register'))
    else:
        return render(request,"registration.html")


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password')
            return HttpResponseRedirect(reverse('login_user'))


    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('Home')



