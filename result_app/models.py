from django.db import models
from .managers import ResultManager
from profile_app.models import Profile
from compatition_app.models import Compatition
from .managers import ResultManager
# Create your models here.

class Result(models.Model):
    player          = models.ForeignKey(Profile , on_delete=models.CASCADE,related_name='player_id')
    compatition     = models.ForeignKey(Compatition,on_delete=models.CASCADE,related_name='compatition_id')
    place           = models.IntegerField()
    status          = models.CharField(max_length=250,blank=True, null=True)
    point           = models.IntegerField()
    objects         = ResultManager()   

  
    def __str__(self):
        return self.player.first_name + " | " + self.player.last_name + " | " + self.compatition.name +"|" + str(self.place )+" | " + str(self.point)