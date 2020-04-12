from django.db import models
from result_app.models import Result


        
class RankQuerySet(models.QuerySet):
    pass
    # def get_Rank_by_id(id):
    #     return self.filter(id = id)
    def get_rank_by_id(self,id):
        return self.filter(id = id )
    
    
class RankManager(models.Manager):

   # def get_queryset(self):
      #  return ProfileQuerySet(self.model,using=self._db)

    def get_query_set(self):
        return RankQuerySet(self.model)

    # def get_Rank_has_result(self ):
    #     return self.get_query_set().get_Rank_has_result()
  
    def get_rank_by_id(self , id ):
        return self.get_query_set().get_rank_by_id(id = id)