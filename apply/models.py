from django.db import models
import datetime

# Create your models here.
class Apply(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    
    def __str__(self):
        return self.title
