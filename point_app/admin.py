from django.contrib import admin
from .models import Point
# Register your models here.

@admin.register(Point)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id','name','sequence' ,'manual_sequence')
     search_fields = ('name',)
    