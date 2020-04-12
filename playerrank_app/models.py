from django.db           import models
from result_app.models   import Result
from rank_app.models     import Rank
from profile_app.models  import Profile 
from point_app.models    import Point
from category_app.models import Category
from .managers           import PlayerRankManager

# Create your models here.

class PlayerRank(models.Model):
    rank_id          = models.ForeignKey(Rank ,    on_delete=models.CASCADE)
    result_id        = models.ForeignKey(Result ,  on_delete=models.CASCADE)
    player_id        = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    point_id         = models.ForeignKey(Point,    on_delete=models.CASCADE)
    category_id      = models.ForeignKey(Category, on_delete=models.CASCADE)
    total            = models.IntegerField()
    best             = models.IntegerField()
    number           = models.IntegerField(blank=True, null=True)
    objects          = PlayerRankManager()   


    def __str__(self):
        return self.player_id.first_name + " | " + self.player_id.last_name + " | "+ str(self.total) + " | " + str(self.best)