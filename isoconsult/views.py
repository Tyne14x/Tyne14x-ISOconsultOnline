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

def TrainingPage(request):
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
        numtax = request.POST.get('numtax')
        concontact = request.POST.get('con-contact')
        title = request.POST.get('title')
        conphone = request.POST.get('con-phone')
        concusemail = request.POST.get('con-cusemail')
        confax = request.POST.get('con-fax')
        reqtraincourse = request.POST.get('req-train-course')
        nunpartic = request.POST.get('nun-partic')
        datetrain = request.POST.get('date-train')
        addcouse1 = request.POST.get('addcouse1')
        adddate1 = request.POST.get('adddate1')
        addcouse2 = request.POST.get('addcouse2')
        adddate2 = request.POST.get('adddate2')


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
            'numtax' : numtax,
            'con-contact' : concontact,
            'title' : title,
            'con-phone' : conphone,
            'con-cusemail' : concusemail,
            'con-fax' : confax,
            'req-train-course' : reqtraincourse,
            'nun-partic' : nunpartic,
            'date-train' : datetrain,
            'addcouse1' : addcouse1,
            'adddate1' : adddate1,
            'addcouse2': addcouse2,
            'adddate2' : adddate2,


        }
        body = '''
        Company :{}
        Address :{}  
        Contact :{}     Position :{}     
        Phone :{}       Email :{}       Fax :{}
        
        Billing to:
        (ออกใบเสร็จรับเงินให้)
        Company: {}
        Address: {}
        Tax id: {}      Contact: {}     Title: {}
        Phone :{}       Email :{}       Fax :{}

        Request for training course :
        (ระบุหลักสูตรที่ต้องการ)    {}
        The number of participants: {}      Required date of training: {}
        Request for other courses ระบุหลักสูตรอื่นๆ (หากมี):
        1.Course 1  {}                    Required date: {}
        2.Course 2  {}                    Required date: {}
        '''.format(data['company'],data['address'],data['contact'],data['position'],data['phone'],
        data['cusemail'],data['fax'],data['con-company'],data['con-address'],data['numtax'],data['con-contact'],
        data['title'],data['con-phone'],data['con-cusemail'],data['con-fax'],data['req-train-course'],
        data['nun-partic'],data['date-train'],data['addcouse1'],data['adddate1'],data['addcouse2'],data['adddate2'])

        send_mail('Contact Form',body, '', [cusemail])#('subject',เนื้อหา,อีเมลล์ที่ส่ง)
    return render(request, 'iso/training.html',{})

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