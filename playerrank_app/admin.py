from django.contrib import admin
from .models import PlayerRank
# Register your models here.
@admin.register(PlayerRank)
class CategoryAdmin(admin.ModelAdmin):
    def get_player_first_name(self, obj):
        return obj.result_id.player.first_name
    def get_player_last_name(self, obj):
        return obj.result_id.player.last_name
    
    


    list_display = ('id','get_player_first_name','get_player_last_name','total','best')