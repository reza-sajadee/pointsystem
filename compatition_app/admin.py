from django.contrib import admin
from .models import Compatition

# Register your models here.



@admin.register(Compatition)
class CategoryAdmin(admin.ModelAdmin):
    def get_category_name(self, obj):
        return obj.category_id.name
    def get_category_gender(self, obj):
        return obj.category_id.gender
    def get_category_age(self, obj):
        return obj.category_id.age
    def get_point_name(self, obj):
        return obj.point_system_id.name


    list_display = ('id','name','get_category_name','get_category_gender','get_category_age','get_point_name')
    #list_filter = ('gender','age',)
    #search_fields = ('name','category_id__name',)
    #list_select_related = ['category_id__name']