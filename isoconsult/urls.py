from django.urls import path, include
from .views import HomePage, AboutPage, TrainingPage ,Register ,BlogPage ,ContactPage #ดึงฟังก์ชันจาก views มา

urlpatterns = [
    # localhost:8000/
    path('',HomePage,name='home-page'),
    path('about/',AboutPage,name='about-page'),
    path('training/',TrainingPage,name='training-page'),
    path('register/',Register,name='register-page'),
    path('blog/',BlogPage,name='blog-page'),
    path('contact/',ContactPage,name='contact-page'),
]
