from sre_parse import Verbose

from django.db import models
from django.db.models.fields.related import ForeignKey


from category_app.models import Category
from point_app.models import Point
from profile_app.models import Profile

from .managers import CompatitionManager

# Create your models here.
yearList = (
    (1398,1398),
    (1399,1399),
    (1400,1400),
    (1401,1401),
    (1402,1402),
    (1403,1403),
    (1404,1404),
    (1405,1405),
)
mounthList =(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
)
dayList =(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
    (13,13),
    (14,14),
    (15,15),
    (16,16),
    (17,17),
    (18,18),
    (19,19),
    (20,20),
    (21,21),
    (22,22),
    (23,23),
    (24,24),
    (25,25),
    (26,26),
    (27,27),
    (28,28),
    (29,29),
    (30,30),
    (31,31),
    
)


class Compatition(models.Model):
    name               = models.CharField(max_length=30)
    category_id        = models.ForeignKey(Category, on_delete=models.CASCADE)
    point_system_id    = models.ForeignKey(Point, on_delete=models.CASCADE)
    head_judge         = models.ForeignKey(Profile,on_delete=models.CASCADE ,related_name="Creator")
    logo               = models.ImageField(upload_to='pic',blank=True, null=True)
    judges             = models.ManyToManyField(Profile,related_name='judges') 
    year               = models.IntegerField(choices=yearList)
    mounth             = models.IntegerField(choices=mounthList)
    day                = models.IntegerField(choices=dayList)
    result             = models.BooleanField(default=False)
    date               = models.DateField(blank=True, null=True)
        
    objects = CompatitionManager()   

    def __str__(self):
        return self.name + '|' + self.category_id.name + '|' + self.category_id.gender + '|' + self.category_id.age+ '|' + self.point_system_id.name