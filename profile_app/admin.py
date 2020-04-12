from django.contrib import admin
from .models import Profile
from .forms import UserAdminCreationForm, UserAdminChangeForm
# Register your models here.
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin






@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('isf_id','first_name','last_name' ,'admin','judge','player')
    list_filter = ('admin','judge','player')
    fieldsets = (
        (None, {'fields': ('isf_id', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','email','country_names','city_name','phone_number','profile_image','club','cridit_card')}),
        ('Permissions', {'fields': ('admin','judge','player','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    '''def get_username(self, obj):
        return obj.isf_id.username
    def get_first_name(self, obj):
        return obj.isf_id.first_name
    def get_last_name(self, obj):
        return obj.isf_id.last_name'''
    
       
        
    