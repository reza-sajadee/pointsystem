from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import CompatitionCreateForm
from .models import Compatition

# Create your views here.


#compatition Classes .
class CompatitionDeleteView(View):
    template_name = "delete.html"
    def get_obj(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Compatition,id = id)
        return obj
    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            header_title  = "Delete Compatition "
            discribtion   = "do you want to delete " + obj.name + " " + obj.category_id.name + " " +  obj.category_id.gender + obj.category_id.age + " Compatition  ?"
            icon_name     = "delete_forever"
            context       = {'object': obj, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
    def post(self, request,id=None ,*args, **kwargs):
        context = {}
        obj = self.get_obj()
        if obj is not None:
            obj.delete()
            messages.warning(request,'Compatition Successfully Deleted')
            context['object']=None
            return redirect('CompatitionListView')
        return render(request,self.template_name,context)

class CreateCompatitionView(View):
    template_name = "register.html"
    
    def get(self, request, *args, **kwargs):
        form = CompatitionCreateForm()
        header_title  = "Create Compatition"
        discribtion   = "Create New Compatition "
        icon_name     = "person_add"
        contex = {'form': form, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,contex)


    def post(self, request, *args, **kwargs):
        form = CompatitionCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your compatition was Create Successfully !')
            return redirect('CompatitionListView')
        else :
            messages.error(request,'Your compatition was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class CompatitionView(View):
    template_name = "detail.html"
    def get(self, request,id=None ,*args, **kwargs):
        if id is not None:
            obj = get_object_or_404(Compatition,id = id)
            context = {'object': obj}
        
        
        return render(request,self.template_name,context)

class CompatitionListView(View):
    template_name = "compatition_list.html"
    queryset = None
    queryset = Compatition.objects.all()
    #queryset = Profile.objects.get_all_compatitions()
    def get(self, request ,*args, **kwargs):
        header_title  = "Compatition Data Table"
        discribtion   = "Compatition Table "
        icon_name     = "table_chart"
        context = {'object_list':self.queryset , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)


class CompatitionUpdateView(View):
    template_name = "update.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Compatition,id = id)
        return obj

    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = CompatitionCreateForm(instance=obj)
            obj = get_object_or_404(Compatition,id = id)
            context = {'form': form,'object':obj}

        return render(request,self.template_name,context)
    
    def post(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = CompatitionCreateForm(request.POST or request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            return redirect('CompatitionListView')
            context = {'form': form,'object':obj}
        return render(request,self.template_name,context)
