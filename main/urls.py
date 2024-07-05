# main/urls.p
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
   # path('student/', views.student, name='student'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('admin/', views.admin, name='admin'),
    path('student/', views.student_view, name='student'),
    path('form/', views.form, name='form'),
    path('submit-od-approval/', views.exam, name='submit_od_approval'),
    path('success/', views.success_page, name='success_page'),
]





