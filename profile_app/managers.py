from django.db import models
from django.contrib.auth.models import BaseUserManager


        
class ProfileQuerySet(models.QuerySet):
    #player queryset
    def get_all_players(self):
        return self.filter(player=True)
    def get_player_by_isf_id(self ,isf_id ):
        return self.filter(isf_id=isf_id)
    def get_player_by_fullname(self ,first_name,last_name ):
        if  self.filter(first_name = first_name).exists():
            if self.filter(last_name = last_name).exists():
                return self.filter(first_name = first_name).filter(last_name = last_name)[0]
        return None

    #judge queryset :
    
    def get_all_judges(self):
        return self.filter(judge=True)
    def get_judge_by_isf_id(self ,isf_id ):
        return self.filter(isf_id=isf_id)
    def get_judge_by_fullname(self ,first_name,last_name ):
        return self.filter(first_name = first_name)
    
class ProfileManager(BaseUserManager):


   # def get_queryset(self):
      #  return ProfileQuerySet(self.model,using=self._db)

    def get_query_set(self):
        return ProfileQuerySet(self.model)

    #player managers :

    def get_all_players(self, *args, **kwargs):
        return self.get_query_set().get_all_players(*args, **kwargs)
    def get_player_by_isf_id(self,isf_id ):
        return self.get_query_set().get_player_by_isf_id(isf_id)
    def get_player_by_fullname(self,first_name , last_name ):
        return self.get_query_set().get_player_by_fullname(first_name , last_name)
    
    #judge managers :

    def get_all_judges(self, *args, **kwargs):
        return self.get_query_set().get_all_judges(*args, **kwargs)
    def get_judge_by_isf_id(self,isf_id ):
        return self.get_query_set().get_judge_by_isf_id(isf_id)
    def get_judge_by_fullname(self,first_name , last_name ):
        return self.get_query_set().get_judge_by_fullname(first_name , last_name)

  #  def get_players(self):
       # return self.get_queryset().get_players()

    def create_user(self, isf_id , first_name , last_name ,password=None,is_judge=False, is_player=False, is_admin=False, is_active=True,is_staff = False):
        if not first_name:
            raise ValueError("Users must have first name")
        if not last_name:
            raise ValueError("Users must have last name")
        if not password:
            raise ValueError("Users must have password")
         
        user_obj = self.model(
            isf_id 
        )
        
        user_obj.first_name     = first_name
        user_obj.last_name      = last_name
        user_obj.judge          = is_judge
        user_obj.player         = is_player
        user_obj.admin          = is_admin
        user_obj.active         = is_active
        user_obj.staff          = is_staff

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_judgeuser(
        self, isf_id , first_name , last_name ,
        password=None,is_judge=True, is_player=False,
        is_admin=False, is_active=True,is_staff = False,):
        if not first_name:
            raise ValueError("Users must have first name")
        if not last_name:
            raise ValueError("Users must have last name")
        if not password:
            raise ValueError("Users must have password")
         
        user_obj = self.model(
            isf_id 
        )
        
        user_obj.first_name     = first_name
        user_obj.last_name      = last_name
        user_obj.judge          = is_judge
        user_obj.player         = is_player
        user_obj.admin          = is_admin
        user_obj.active         = is_active
        user_obj.staff          = is_staff

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj
    
    def create_playeruser(
        self, isf_id , first_name , last_name ,
        password=None,is_judge=False, is_player=True,
        is_admin=False, is_active=True,is_staff = False,):
        if not first_name:
            raise ValueError("Users must have first name")
        if not last_name:
            raise ValueError("Users must have last name")
        if not password:
            raise ValueError("Users must have password")
         
        user_obj = self.model(
            isf_id 
        )
        
        user_obj.first_name     = first_name
        user_obj.last_name      = last_name
        user_obj.judge          = is_judge
        user_obj.player         = is_player
        user_obj.admin          = is_admin
        user_obj.active         = is_active
        user_obj.staff          = is_staff

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, isf_id , first_name , last_name ,password=None,is_judge=False, is_player=True, is_admin=False, is_active=True,is_staff = True):
        if not first_name:
            raise ValueError("Users must have first name")
        if not last_name:
            raise ValueError("Users must have last name")
        if not password:
            raise ValueError("Users must have password")
         
        user_obj = self.model(
            isf_id 
        )
        user_obj.isf_id         = isf_id
        user_obj.first_name     = first_name
        user_obj.last_name      = last_name
        user_obj.judge          = is_judge
        user_obj.player         = is_player
        user_obj.admin          = is_admin
        user_obj.active         = is_active
        user_obj.staff          = is_staff

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj


    def create_superuser(self, isf_id , first_name , last_name ,password=None,is_judge=False, is_player=True, is_admin=True, is_active=True,is_staff = True):
        if not first_name:
            raise ValueError("Users must have first name")
        if not last_name:
            raise ValueError("Users must have last name")
        if not password:
            raise ValueError("Users must have password")
         
        user_obj = self.model(
            isf_id 
        )
        user_obj.isf_id         = isf_id
        user_obj.first_name     = first_name
        user_obj.last_name      = last_name
        user_obj.judge          = is_judge
        user_obj.player         = is_player
        user_obj.admin          = is_admin
        user_obj.active         = is_active
        user_obj.staff          = is_staff

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    
