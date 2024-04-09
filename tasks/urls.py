from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('usersform/', usersForm, name='users-form'),
    path('userslist/', usersList, name='users-list'),    
    path('tasksform/', tasksForm, name='tasks-form'),
    path('taskslist/', taskList, name='tasks-list'),
    
    path('assigntask/', assign_task, name='assign-task'),
    path('assignlist/', assign_list, name='assign-list'),
    
]