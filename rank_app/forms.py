from django import forms
from django.db import models
from .models import Rank




class RankCreateForm(forms.ModelForm):
    
    

    class Meta:
        model = Rank
        exclude = ('player_id','rank')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_mounth'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_day'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_mounth'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_day'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['numbers'].widget.attrs.update({'class': 'form-control'})
        

        self.fields['category_id'].Label                ='Select the Category'
        self.fields['numbers'].Label                    ='Select the Category'
        self.fields['start_year'].Label                 ='Select the Category'
        self.fields['start_mounth'].Label               ='Select the Category'
        self.fields['start_day'].Label                  ='Select the Category'
        self.fields['end_year'].Label                   ='Select the Category'
        self.fields['end_mounth'].Label                 ='Select the Category'
        self.fields['end_day'].Label                    ='Select the Category'
        
   
    
         # TODO Validation
    


        
