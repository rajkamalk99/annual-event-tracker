from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30, unique=True)
    idea = models.CharField(max_length=150)
    status = models.CharField(max_length=9,choices=(('ongoing', 'OnGoing'),('completed', 'Completed'),('onhold', 'OnHold')))
    created_on = models.DateTimeField(auto_now_add=True)
    project_head = models.ForeignKey(User, null=True)   


    def __str__(self):
        return self.name