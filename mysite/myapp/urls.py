from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='Home'),
    path('Home/', views.index, name='base'),
    path('about', views.about,name='about'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('doctors', views.doctors, name='doctors'),
    path('department', views.department, name='department'),
    path('career', views.career_view, name='career'),
    path('register',views.regis,name="register"),
    path('login_user',views.login_user,name='login_user'),
    path('logout',views.logout,name='logout'),


]
