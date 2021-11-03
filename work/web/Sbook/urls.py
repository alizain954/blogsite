from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('singup/', views.singup, name='singup'),
    path('datainsert/', views.datainsert, name='datainsert'),
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('conatct/', views.contact, name='contact'),
    path('create/', views.create, name='create'),
    path('readmore/<int:id>', views.readmore, name='readmore')

]
