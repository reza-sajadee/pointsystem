from django.db import models



class PlayerRankQuerySet(models.QuerySet):
  def get_playerrank_by_player(self,player_id):
        return self.filter(player_id = player_id)
  def get_playerrank_by_rank_id(self,rank_id):
        return self.filter(rank_id__id = rank_id)
  
  
class PlayerRankManager(models.Manager):

   # def get_queryset(self):
      #  return ProfileQuerySet(self.model,using=self._db)

    def get_query_set(self):
        return PlayerRankQuerySet(self.model).order_by('total')

    def get_playerrank_by_player(self,player_id ):
        return self.get_query_set().get_playerrank_by_player(player_id=player_id)
    def get_playerrank_by_rank_id(self,rank_id ):
        return self.get_query_set().get_playerrank_by_rank_id(rank_id=rank_id)

