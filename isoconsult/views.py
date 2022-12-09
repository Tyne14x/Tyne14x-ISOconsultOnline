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
    if request.method == 'POST':
        company = request.POST.get('company')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        position = request.POST.get('position')
        cusemail = request.POST.get('cusemail')
        phone = request.POST.get('phone')
        fax = request.POST.get('fax')
        concompany = request.POST.get('con-company')
        conaddress = request.POST.get('con-address')

        data = {
            'company' : company,
            'address' : address,
            'contact' : contact,
            'position': position,
            'phone' : phone,
            'cusemail':  cusemail,
            'fax' : fax,
            'con-company' : concompany,
            'con-address' : conaddress,
        }
        message = '''
        Company :{}
        Address :{}  
        Contact :{}     Position :{}     
        Phone :{}       Email :{}       Fax :{}
        
        ออกใบเสร็จรับเงินให้
        Company: {}
        Address: {}
        '''.format(data['company'],data['address'],data['contact'],data['position'],data['phone'],
        data['cusemail'],data['fax'],data['con-company'],data['con-address'])

        send_mail('Contact Form',message, '', [cusemail])#('subject',เนื้อหา,อีเมลล์ที่ส่ง)
    return render(request, 'iso/contact.html',{})

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

def TestPage(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        cusemail = request.POST.get('cusemail')
        phone = request.POST.get('phone')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        message = request.POST.get('message')

        data = {
            'name' : name,
            'cusemail' : cusemail,
            'phone' : phone,
            'contact' : contact,
            'date' : date,
            'message' : message
        }
        message = '''
        Name :{}
        email Customer :{}  Phone :{}    
        Contact :{}
        Date : {}
        message :{}
        '''.format(data['name'], data['cusemail'],data['phone'],data['contact'],data['date'],data['message'])
        send_mail('Contact Form',message, '', [cusemail])#('subject',เนื้อหา,อีเมลล์ที่ส่ง)
    return render(request,'iso/Test.html',{})