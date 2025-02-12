from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_user')
    email = models.CharField(max_length=200,null = False)
class SousAdmin(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='SousAdmin_user')
    email = models.CharField(max_length=200,null = False)
class Employe(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Employee_user')
    email = models.CharField(max_length=200,null = False)
