from django import forms
from django.db import models
from category_app.models import Category



class CategoryCreateForm(forms.ModelForm):

    

    class Meta:
        model = Category
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

        self.fields['name'].Label            ='Select the Category'
        self.fields['gender'].Label          ='Select the Category'
        self.fields['age'].Label             ='Select the Category'
        self.fields['description'].Label     ='Select the Category'
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
        

