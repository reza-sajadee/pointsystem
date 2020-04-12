from django.contrib import admin
from .models import Category
# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id','name','gender' ,'age')
     list_filter = ('gender','age',)
     search_fields = ('gender','age','name',)
    