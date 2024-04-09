from django.shortcuts import render, redirect
from .models import *

from django.http import HttpResponseBadRequest

#--------USERS----------

def usersForm(request):
    if request.method == 'POST':    
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        
        userform = Users.objects.create(
            name=name, 
            email=email, 
            mobile=mobile,
        )
        userform.name= name
        userform.email= email
        userform.mobile= mobile
        userform.save()
        return redirect('users-list')
    else:
        return render(request, 'users_form.html')
     
def usersList(request):
    users = Users.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'users_list.html', context)

#---------TASKS----------

def tasksForm(request):
    if request.method == 'POST':    
        taskDetail = request.POST.get('task_detail')
        taskType = request.POST.get('task_type')
        
        taskform = Task.objects.create(
            taskDetail=taskDetail,
            taskType=taskType,
        )
        taskform.taskDetail= taskDetail
        taskform.taskType= taskType
        taskform.save()
        return redirect('tasks-list')
    else:
        return render(request, 'tasks_form.html')

def taskList(request):
    # user = Users.objects.get(pk=user_id)
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        # 'user': user,
    }
    return render(request, 'tasks_list.html', context)

#-----------AssignTask--------
def assign_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('taskID')
        user_id = request.POST.get('userID')
        
        task = Task.objects.get(pk=task_id)
        user = Users.objects.get(pk=user_id)
        task.user = user
        task.save()
        
        assigned_task = AssignedTask.objects.create(
            user=user,
            task=task
            )
        assigned_task.save()
        return redirect('assign-list')  
    else:
        tasks = Task.objects.all()
        users = Users.objects.all()
        context = {
            'tasks': tasks,
            'users': users,
            }
        return render(request, 'assign_task.html', context)
def assign_list(request):
    assigned_tasks = AssignedTask.objects.all()
    context = {
        'assigned_tasks': assigned_tasks,
        }
    return render(request, 'assign_list.html', context)