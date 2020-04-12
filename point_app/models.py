from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from .managers import PointManager
# Create your models here.
class Point(models.Model):
    name=models.CharField(max_length=30)
    sequence=models.IntegerField()
    manual_sequence = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True, null=True,default='')
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name 

    objects = PointManager()  