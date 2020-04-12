from django import forms
from django.db import models


from .models import Compatition


class CompatitionCreateForm(forms.ModelForm):

    

    class Meta:
        model = Compatition
        fields = '__all__'
        exclude = ('judges','players')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['category_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['point_system_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['mounth'].widget.attrs.update({'class': 'form-control'})
        self.fields['day'].widget.attrs.update({'class': 'form-control'})
        self.fields['head_judge'].widget.attrs.update({'class': 'form-control'})
        self.fields['logo'].widget.attrs.update({'class': 'form-control'})



        



        self.fields['name'].Label                  ='Select the Category'
        self.fields['category_id'].Label           ='Select the Category'
        self.fields['point_system_id'].Label       ='Select the Category'
        self.fields['year'].Label                  ='Select the Category'
        self.fields['mounth'].Label                ='Select the Category'
        self.fields['day'].Label                   ='Select the Category'
        self.fields['head_judge'].Label            ='Select the Category'
        self.fields['logo'].Label                  ='Select the Category'


