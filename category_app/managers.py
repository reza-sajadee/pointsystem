from django.db import models



        
class CategoryQuerySet(models.QuerySet):
    pass
    
class CategoryManager(models.Manager):

   # def get_queryset(self):
      #  return ProfileQuerySet(self.model,using=self._db)

    def get_query_set(self):
        return CategoryQuerySet(self.model)

    #player managers :
