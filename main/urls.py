from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('student-life/', views.student_life, name='student_life'),
    path('news/', views.news, name='news'),
    path('parents/', views.parents, name='parents'),
    path('contact/', views.contact, name='contact'),
] 