from django import forms
from django.db import models
from django.contrib.auth import  get_user_model
import io
import csv
from .models import Result
from profile_app.models import Profile
from profile_app.forms import UserPlayerCreationForm


class ResultCreateForm(forms.ModelForm):
    
    

    class Meta:
        model = Result
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player'].widget.attrs.update({'class': 'form-control'})
        self.fields['compatition'].widget.attrs.update({'class': 'form-control'})
        self.fields['place'].widget.attrs.update({'class': 'form-control'})
        self.fields['point'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['status'].widget = forms.HiddenInput()
        

        self.fields['point'].Label                 ='Select the Category'
        self.fields['player'].Label                ='Select the Category'
        self.fields['compatition'].Label           ='Select the Category'
        self.fields['place'].Label                 ='Select the Category'
        
   
    
         # TODO Validation
    

class ResultCsvForm(forms.ModelForm):

    data_file = forms.FileField()    
    class Meta:
        model = Profile
        fields =['data_file',]

    

        
class ResultCompatitionName(forms.ModelForm):
      class Meta:
        model = Result
        fields =['compatition',]

      def __init__(self, *args, **kwargs):

          super().__init__(*args, **kwargs)
          self.fields['compatition'].widget.attrs.update({'class': 'form-control'})
          self.fields['compatition'].Label                ='Select the Category'
