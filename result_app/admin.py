from django.contrib import admin
from .models import Result
# Register your models here.

@admin.register(Result)
class CategoryAdmin(admin.ModelAdmin):
    def get_player_first_name(self, obj):
        return obj.player.first_name
    def get_player_last_name(self, obj):
        return obj.player.last_name
    def get_compatition_name(self, obj):
        return obj.compatition.name
    def get_compatition_category(self, obj):
        return obj.compatition.category_id


    list_display = ('id','get_player_first_name','get_player_last_name','get_compatition_name','place')
    