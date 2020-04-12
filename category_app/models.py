from django.db import models
from .managers import CategoryManager
# Create your models here.
genderList = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('All', 'All'),
    )

class Category(models.Model):

    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=6,choices=genderList)
    age=models.CharField(max_length=30)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name + " | " + self.gender + " | " + self.age
    
    objects = CategoryManager()    