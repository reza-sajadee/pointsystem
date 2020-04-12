from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import CategoryCreateForm
from .models import Category

# Create your views here.



#category Classes .
class CategoryDeleteView(View):
    template_name = "delete.html"
    def get_obj(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Category,id = id)
        return obj
    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            header_title  = "Delete Category System"
            discribtion   = "do you want to delete " + obj.name + " " + obj.gender + " " + obj.age + " Category  ?"
            icon_name     = "delete_forever"
            context       = {'object': obj, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
    def post(self, request,id=None ,*args, **kwargs):
        context = {}
        obj = self.get_obj()
        if obj is not None:
            obj.delete()
            messages.warning(request,'Category Successfully Deleted')
            context['object']=None
            return redirect('CategoryListView')
        return render(request,self.template_name,context)

class CreateCategoryView(View):
    template_name = "register.html"
    
    def get(self, request, *args, **kwargs):
        form = CategoryCreateForm()
        header_title  = "Create Category"
        discribtion   = "Create New Category"
        icon_name     = "person_add"
        contex = {'form': form, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,contex)


    def post(self, request, *args, **kwargs):
        form = CategoryCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your category was Create Successfully !')
            return redirect('CategoryListView')
        else :
            messages.error(request,'Your category was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class CategoryView(View):
    template_name = "detail.html"
    def get(self, request,id=None ,*args, **kwargs):
        if id is not None:
            obj = get_object_or_404(Category,id = id)
            context = {'object': obj}
        
        
        return render(request,self.template_name,context)

class CategoryListView(View):
    template_name = "category_list.html"
    queryset = None
    queryset = Category.objects.all()
    #queryset = Profile.objects.get_all_categorys()
    def get(self, request ,*args, **kwargs):
        header_title  = "Category Data Table"
        discribtion   = "Category Table "
        icon_name     = "table_chart"
        context = {'object_list':self.queryset , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)

class CategoryUpdateView(View):
    template_name = "update.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Category,id = id)
        return obj

    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = CategoryCreateForm(instance=obj)
            obj = get_object_or_404(Category,id = id)
            context = {'form': form,'object':obj}

        return render(request,self.template_name,context)
    
    def post(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = CategoryCreateForm(request.POST or request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            return redirect('CategoryListView')
            context = {'form': form,'object':obj}
        return render(request,self.template_name,context)
