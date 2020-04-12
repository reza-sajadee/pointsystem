from os.path import split

from django.db import models


class PointQuerySet(models.QuerySet):
    def get_point_by_name(self ,name ):
        return self.filter(name=name)
    
class PointManager(models.Manager):

   # def get_queryset(self):
      #  return ProfileQuerySet(self.model,using=self._db)

    def get_query_set(self):
        return PointQuerySet(self.model)

    def get_point_by_name(self,name  ):
        return self.get_query_set().get_point_by_name(name= name)
    #player managers :
