
from django.conf import settings

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from result_app.models import Result

from .forms import (ProfileRegisterForm, UserAdminCreationForm,
                    UserJudgeChangeForm, UserJudgeCreationForm, UserLoginForm,
                    UserPlayerChangeForm, UserPlayerCreationForm,
                    UserRegisterForm)
from .models import Profile




# Create your views here.
class profileLogin(View):
    template_name = "login.html"
    def get(self, request,id=None ,*args, **kwargs):
        form = UserLoginForm()
        context = {'form':form}
        return render(request,"login.html",context)
    
    def post(self, request,id=None ,*args, **kwargs):
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            isf_id = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(isf_id=isf_id , password = password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request,'Login was successfully !')
            return redirect('dashboard')
        else:
            messages.error(request,'User is not exist or password is wrong !')
            context = {'form':form}
            return render(request,"login.html",context)


#player Classes .
class PlayerDeleteView(View):
    template_name = "delete.html"
    def get_obj(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Profile,isf_id = id)
        return obj
    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            header_title  = "Delete Player Profile"
            discribtion   = "do you want to delete  " + obj.first_name + "  " + obj.last_name + " Player Profile  ?"
            icon_name     = "delete_forever"
            context       = {'object': obj, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
    def post(self, request,id=None ,*args, **kwargs):
        context = {}
        obj = self.get_obj()
        if obj is not None:
            obj.delete()
            messages.warning(request,'Profile Successfully Deleted')
            context['object']=None
            return redirect('PlayerListView')
        return render(request,self.template_name,context)

class CreatePlayerView(View):
    template_name = "register.html"
    
    def get(self, request, *args, **kwargs):
        header_title  = "Create Profile"
        discribtion   = "Create Profile for Player"
        icon_name     = "person_add"
        form = UserPlayerCreationForm()
        contex = {'form': form , 'header_title ':header_title ,'discribtion': discribtion,'icon_name': icon_name  }
        return render(request,self.template_name,contex)


    def post(self, request, *args, **kwargs):
        form = UserPlayerCreationForm(request.POST or None, request.FILES or None)
        if form.is_valid():

            form.save()
            messages.success(request,'Your Profile was Create Successfully !')
            new_user = authenticate(username=form.cleaned_data['isf_id'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return render(request,"dashboard.html")
        else :
            messages.error(request,'Your Profile was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class PlayerView(View):
    template_name = "profile.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Profile,isf_id = id)
            
        return obj
    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            results = Result.objects.get_Result_player_id(player_id = id)
            form = UserPlayerChangeForm(instance=obj)
            obj = get_object_or_404(Profile,isf_id = id)

            
            
            context = {'form': form,'object':obj,'results':results}

        return render(request,self.template_name,context)
    

class PlayerListView(View):
    template_name = "player_list.html"
    queryset = None
    
    queryset = Profile.objects.filter(
        player=True
    )
    #queryset = Profile.objects.get_all_players()
    def get(self, request ,*args, **kwargs):
        title = ['ISF ID' , 'First Name','Last Name','City','Club','Country','Phone Number','Edit','Delete']
        # object_list=[]
        # for obj in self.queryset:
        #     data = {
        #         "ISF ID":obj.isf_id, "First Name":obj.first_name,
        #         "Last Name":obj.last_name,"City":obj.city_name,
        #         "Club":obj.club,"Country":obj.country_names,"Phone Number":obj.phone_number,
        #         "Edit":'<td><button type="button" rel="tooltip" title="" class="btn btn-secondary btn-sm" data-original-title="Edit Category"> <a href="#"> <i class="material-icons">edit</i></a> </button></td>',
        #         "Delete":'<td><button type="button" rel="tooltip" title="" class="btn btn-danger btn-sm" data-original-title="Edit Category"> <a href="#"> <i class="material-icons">edit</i></a> </button></td>'
                
        #         } 
        #     object_list.append(data)
        header_title  = "Profile Player Data Table"
        discribtion   = "Profile Player Table "
        icon_name     = "table_chart"
        context = {'object_list':self.queryset ,'object_title':title, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)


class PlayerUpdateView(View):
    template_name = "profile.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Profile,isf_id = id)
            
        return obj

    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            results = Result.objects.get_Result_player_id(player_id = id)
            form = UserPlayerChangeForm(instance=obj)
            obj = get_object_or_404(Profile,isf_id = id)

            
            
            context = {'form': form,'object':obj,'results':results}

        return render(request,self.template_name,context)
    
    def post(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = UserPlayerChangeForm(request.POST or request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            return redirect('PlayerListView')
            
            context = {'form': form,'object':obj}
        return render(request,self.template_name,context)
    
#Judge Classes .

#judge Classes .
class JudgeDeleteView(View):
    template_name = "delete.html"
    def get_obj(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Profile,isf_id = id)
        return obj
    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            header_title  = "Delete Judge Profile"
            discribtion   = "do you want to delete  " + obj.first_name + "  " + obj.last_name + " Judge Profile  ?"
            icon_name     = "delete_forever"
            context       = {'object': obj, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
    def post(self, request,id=None ,*args, **kwargs):
        context = {}
        obj = self.get_obj()
        if obj is not None:
            obj.delete()
            messages.warning(request,'Profile Successfully Deleted')
            context['object']=None
            return redirect('JudgeListView')
        return render(request,self.template_name,context)

class CreateJudgeView(View):
    template_name = "register.html"
    
    def get(self, request, *args, **kwargs):
        header_title  = "Create Profile"
        discribtion   = "Create Profile for Judge"
        icon_name     = "person_add"
        if not request.user.is_authenticated:
            messages.warning(request,'You must be Login !!!')

            return redirect(request,'login.html')
        form = UserJudgeCreationForm()
        contex = {'form': form, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,contex)


    def post(self, request, *args, **kwargs):
        form = UserJudgeCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile was Create Successfully !')
            new_user = authenticate(username=form.cleaned_data['isf_id'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return render(request,"dashboard.html")
        else :
            messages.error(request,'Your Profile was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class JudgeView(View):
    template_name = "detail.html"
    def get(self, request,id=None ,*args, **kwargs):
        if id is not None:
            obj = get_object_or_404(Profile,isf_id = id)
            context = {'object': obj}
        
        
        return render(request,self.template_name,context)

class JudgeListView(View):
    template_name = "judge_list.html"
    queryset = None
    queryset = Profile.objects.filter(
        judge=True
    )
    #queryset = Profile.objects.get_all_judges()
    def get(self, request ,*args, **kwargs):
        header_title  = "Profile Judge Data Table"
        discribtion   = "Profile Judge Table "
        icon_name     = "table_chart"
        context = {'object_list':self.queryset , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)

class JudgeUpdateView(View):
    template_name = "update.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Profile,isf_id = id)
        return obj

    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = UserJudgeChangeForm(instance=obj)
            obj = get_object_or_404(Profile,isf_id = id)
            context = {'form': form,'object':obj}

        return render(request,self.template_name,context)
    
    def post(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = UserJudgeChangeForm(request.POST or request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            return redirect('JudgeListView')
            context = {'form': form,'object':obj}
        return render(request,self.template_name,context)
    




# def register_view(request):
    
#     next = request.GET.get('next')
#     userForm = UserPlayerCreationForm(request.POST or None,request.FILES or None)
  
#     if userForm.is_valid():
#         user = userForm.save(commit=False)
        
#         password = userForm.cleaned_data.get('password')
#         user.set_password(password)
#         new_user = authenticate(isf_id=user.isf_id , password = password)
#         login(request,new_user)
        
#         if next:
#             return redirect(next)
#         return redirect('../../dashboard')
#     context ={
#         'userForm':userForm,

#     }

#     return render(request,"Register.html",context)



def logout_views(request):
    logout(request)
    messages.success(request,'Logout Succeesfully')
    return redirect('../')



# def login_view(request):


#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():

#         isf_id = form.cleaned_data.get('isf_id')
#         password = form.cleaned_data.get('password')
#         user = authenticate(isf_id=isf_id , password = password)
#         login(request,user)
#         messages.success(request,'Login was successfully !')
#         if next:
#             return redirect(next)
#         return redirect('../')
#     context ={
#         'form':form,

#     }

#     return render(request,"login.html",context)
