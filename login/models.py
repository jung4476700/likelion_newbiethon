from django.db import models

# Create your models here.
class Login(models.Model):
    login_id = models.CharField(max_length=20)
    login_password= models.CharField(max_length=20)
    