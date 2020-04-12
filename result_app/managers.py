from datetime import datetime

from django.db import models

from compatition_app.models import Compatition


class ResultQuerySet(models.QuerySet):
  def get_Compatition_result(self , compatition):
    return self.filter(compatition = compatition)
  def get_Compatition_filter_category(self , category):
    return self.filter(compatition__category_id__id = category)
  def get_Result_player_id(self , player_id):
    return self.filter(player__isf_id = player_id)
  def get_Result_category_date_filter(self , rank):
    category_id   = rank.cleaned_data.get('category_id')
    start_year    =  rank.cleaned_data.get('start_year')
    start_mounth  =  rank.cleaned_data.get('start_mounth')
    start_day     =  rank.cleaned_data.get('start_day')
    start = datetime(year=start_year,month=start_mounth,day=start_day)
    end_year      =  rank.cleaned_data.get('end_year')
    end_mounth    =  rank.cleaned_data.get('end_mounth')
    end_day       =  rank.cleaned_data.get('end_day')
    end = datetime(year=end_year,month=end_mounth,day=end_day)
    return self.filter(
      compatition__category_id = category_id,
      compatition__date__year__range = (start_year,end_year)
      )
      
    
  
class ResultManager(models.Manager):

   # def get_queryset(self):
      #  return ProfileQuerySet(self.model,using=self._db)

    def get_query_set(self):
        return ResultQuerySet(self.model).order_by('status')

    def get_Compatition_result(self ,compatition):
        return self.get_query_set().get_Compatition_result(compatition = compatition)
    def get_Compatition_filter_category(self ,category):
        return self.get_query_set().get_Compatition_filter_category(category = category)
    def get_Result_category_date_filter(self ,rank):
        return self.get_query_set().get_Result_category_date_filter(rank = rank)
    def get_Result_player_id(self ,player_id):
        return self.get_query_set().get_Result_player_id(player_id = player_id)
  
   
    #player managers :
