from django.db import models

# Create your models here.
class Polls(models.Model):
    title=models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    pub_date=models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    video_title=models.CharField(max_length=200)
    video_key=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.title
    
    
