from django.db import models

class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    
    # class Meta: 
    #     ordering = ('name')
    # def __str__(self):
    #     return self.name    
        
        
class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(Users, related_name = "task_UserID", on_delete=models.CASCADE, null=True)
    taskDetail = models.CharField(max_length=100, null=True, blank=True)
    taskType = models.CharField(max_length=100, null=True, blank=True)
    
class AssignedTask(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)    
