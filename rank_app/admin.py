from django.contrib import admin
from .models import Rank
# Register your models here.

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    def get_player_first_name(self, obj):
        return obj.player_id.first_name
    def get_player_last_name(self, obj):
        return obj.player_id.last_name
    def get_start_date(self, obj):
        return str(obj.start_year) +'/'+ str(obj.start_mounth) +'/'+  str(obj.start_day)
    def get_end_date(self, obj):
        return str(obj.end_year) +'/'+ str(obj.end_mounth) +'/'+  str(obj.end_day)
    def get_category_name(self, obj):
        return obj.category_id.name
    def get_category_gender(self, obj):
        return obj.category_id.gender
    def get_category_age(self, obj):
        return obj.category_id.age

    
    list_display = (
        'get_category_name','get_category_gender','get_category_age',
        'get_start_date','get_end_date'
        )