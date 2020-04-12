from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import PointCreateForm
from .models import Point

# Create your views here.



#point Classes .
class PointDeleteView(View):
    template_name = "delete.html"
    def get_obj(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Point,id = id)
        return obj
    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            header_title  = "Delete Point System"
            discribtion   = "do you want to delete " + obj.name + " Point System ?"
            icon_name     = "delete_forever"
            context       = {'object': obj, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
    def post(self, request,id=None ,*args, **kwargs):
        context = {}
        obj = self.get_obj()
        if obj is not None:
            obj.delete()
            messages.warning(request,'Point Successfully Deleted')
            context['object']=None
            return redirect('PointListView')
        return render(request,self.template_name,context)

@method_decorator(csrf_exempt, name='dispatch')
class CreatePointView(View):
    template_name = "create_point.html"
    
    def get(self, request, *args, **kwargs):
        form = PointCreateForm()
        header_title  = "Create Point"
        discribtion   = "You can defination new point System"
        icon_name     = "person_add"
        contex = {'form': form, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,contex)

    
    def post(self, request, *args, **kwargs):
        form = PointCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your point was Create Successfully !')
            
            return redirect('PointListView')
        else :
            messages.error(request,'Your point was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class PointView(View):
    template_name = "detail.html"
    def get(self, request,id=None ,*args, **kwargs):
        if id is not None:
            obj = get_object_or_404(Point,id = id)
            context = {'object': obj}
        
        
        return render(request,self.template_name,context)

class PointListView(View):
    template_name = "point_list.html"
    queryset = None
    queryset = Point.objects.all()
    #queryset = Profile.objects.get_all_points()
    def get(self, request ,*args, **kwargs):
        header_title  = "Point System Data Table"
        discribtion   = "Point System Table "
        icon_name     = "table_chart"
        context = {'object_list':self.queryset , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)

class PointUpdateView(View):
    template_name = "create_point.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Point,id = id)
        return obj

    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = PointCreateForm(instance=obj)
            obj = get_object_or_404(Point,id = id)
            context = {'form': form,'object':obj}

        return render(request,self.template_name,context)
    
    def post(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = PointCreateForm(request.POST or request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            return redirect('PointListView')
            context = {'form': form,'object':obj}
        return render(request,self.template_name,context)
