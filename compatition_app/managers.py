from django.db import models



        
class CompatitionQuerySet(models.QuerySet):
    def get_Compatition_has_result(self  ):
        return self.filter(result = True)

    def get_Compatition_by_id(self,id):
        return self.filter(id = id)
    
    
class CompatitionManager(models.Manager):

   # def get_queryset(self):
      #  return ProfileQuerySet(self.model,using=self._db)

    def get_query_set(self):
        return CompatitionQuerySet(self.model)

    def get_Compatition_has_result(self ):
        return self.get_query_set().get_Compatition_has_result()
    def get_Compatition_by_id(self,id ):
        return self.get_query_set().get_Compatition_by_id(id=id)
    #player managers :
