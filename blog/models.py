from django.db import models

# Create your models here.
class Post(models.Model):
    """docstring for Post."""
    title=models.CharField(max_length=250)
    content=models.TextField()
    
    def __str__(self):
        return self.title
  
        
