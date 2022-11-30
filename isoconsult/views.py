from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

#ฟังก์ชัน HomePage
def HomePage(request):
    return render(request, 'iso/home.html')

def AboutPage(request):
    return render(request, 'iso/about.html')

def ContactPage(request):
    return render(request, 'iso/contact.html')

def TestPage(request):
    return render(request, 'iso/Test.html')

def FormPage(request):
    return render(request, 'iso/form.html')

def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        return redirect('login')

    return render(request, 'iso/register.html')

def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
        'Contact Form',
        message,
        'settings.EMAIL_HOST_USER',
        [email],
        fail_silently=False)
    return render(request, 'index.html')