from django.urls import path, include
from .views import HomePage, AboutPage, ContactPage ,Register,FormPage, TestPage #ดึงฟังก์ชัน HomePage มาโชว์

urlpatterns = [
    # localhost:8000/
    path('',HomePage,name='home-page'),
    path('about/',AboutPage,name='about-page'),
    path('contact/',ContactPage,name='contact-page'),
    path('register/',Register,name='register-page'),
    path('form/',FormPage,name='form-page'),
    path('test/',TestPage,name='test-page'),
]
