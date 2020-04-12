from django import forms
from django.db import models
from .models import PlayerRank




class PlayerRankCreateForm(forms.ModelForm):
    
    

    class Meta:
        model = PlayerRank
        exclude = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

     


        self.fields['rank_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['result_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['player_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['point_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['category_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['total'].widget.attrs.update({'class': 'form-control'})
        self.fields['best'].widget.attrs.update({'class': 'form-control'})
        
        

        self.fields['rank_id'].Label              ='Select the Category'
        self.fields['result_id'].Label            ='Select the Category'
        self.fields['player_id'].Label            ='Select the Category'
        self.fields['point_id'].Label             ='Select the Category'
        self.fields['category_id'].Label          ='Select the Category'
        self.fields['total'].Label                ='Select the Category'
        self.fields['best'].Label                 ='Select the Category'
       
        
   
    
         # TODO Validation
    


        
