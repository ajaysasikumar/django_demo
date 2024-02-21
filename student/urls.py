from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),

    path('student_create/', views.create,name='create'),
    path('view_students/', views.view,name='view'),
    path('edit/<int:pk>', views.edit,name='edit'),
    path('Academics/<int:pk>', views.academics,name='Academics'),
    path('student_home', views.student_home,name='student_home'),
    path('student_marks/<int:pk>', views.student_marks,name='student_marks'),
    
    path('logout', views.sign_out,name='logout'),
    path('delete/<int:pk>', views.delete,name='delete-user'),
    path('profile/<int:pk>', views.Profile,name='profile'),
    path('admin_message', views.admin_message,name='admin_message'),

    


    
]