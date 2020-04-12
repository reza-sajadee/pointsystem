from django.db import models
from .managers import RankManager
from profile_app.models import Profile
from compatition_app.models import Compatition
from category_app.models import Category

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
class Rank(models.Model):

    category_id              = models.ForeignKey(Category, on_delete=models.CASCADE)

    start_year               = models.IntegerField(choices=yearList)
    start_mounth             = models.IntegerField(choices=mounthList)
    start_day                = models.IntegerField(choices=dayList)
    end_year                 = models.IntegerField(choices=yearList)
    end_mounth               = models.IntegerField(choices=mounthList)
    end_day                  = models.IntegerField(choices=dayList)




    numbers                  = models.IntegerField()
    objects                  = RankManager()   

    def __str__(self):
        return self.category_id.name + " | " + self.category_id.gender + " | "+ self.category_id.age 