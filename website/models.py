from django.db import models

# Create your models here.

class contact(models.Model):
    name= models.CharField(max_length=255)
    email= models.EmailField()
    subject= models.CharField(max_length=255,null=True, blank=True)
    massage= models.TextField()
    creatade_date= models.DateField(auto_now_add=True)
    update_date= models.DateField(auto_now=True)
    class Meta():
        ordering = ['-creatade_date']
    
    def __str__(self):
        return self.name
