from django import forms
from django.db import models
from .models import Point



class PointCreateForm(forms.ModelForm):

    

    class Meta:
        model = Point
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['sequence'].widget.attrs.update({'class': 'form-control'})
        self.fields['manual_sequence'].widget = forms.HiddenInput()
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['name'].Label            ='Select the Point'
        self.fields['sequence'].Label        ='Select the Point'
        self.fields['description'].Label     ='Select the Point'
    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     if name = "":
    #         raise forms.ValidationError("Name is a requared ")
    #     return name
    # def clean_gender(self):
    #     gender = self.cleaned_data.get("gender")
    #     if gender = None:
    #         raise forms.ValidationError("gender is a requared ")
    #     return name
    # def clean_age(self):
    #     age = self.cleaned_data.get("age")
    #     if age = None:
    #         raise forms.ValidationError("age is a requared ")
    #     return age
        

