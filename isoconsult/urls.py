from django.urls import path, include
from .views import HomePage, AboutPage, TrainingPage ,Register,FormPage, TestPage #ดึงฟังก์ชันจาก views มา

urlpatterns = [
    # localhost:8000/
    path('',HomePage,name='home-page'),
    path('about/',AboutPage,name='about-page'),
    path('training/',TrainingPage,name='training-page'),
    path('register/',Register,name='register-page'),
    path('form/',FormPage,name='form-page'),
    path('test/',TestPage,name='test-page'),
]
