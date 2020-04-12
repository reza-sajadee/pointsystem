import csv
import io
from datetime import datetime

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from point_app.models import Point
from compatition_app.models import Compatition
from profile_app.models import Profile

from .forms import ResultCompatitionName, ResultCreateForm, ResultCsvForm
from .models import Result

# Create your views here.


#result Classes .
class ResultDeleteView(View):
    template_name = "delete.html"
    def get_obj(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Result,id = id)
        return obj
    def get(self, request,id=None ,*args, **kwargs):
        
        
        obj = self.get_obj()
        if obj is not None:
            header_title  = "Delete Result"
            discribtion   = "do you want to delete " + obj.player.first_name + " " + obj.player.last_name + " " + obj.compatition.name + " Result ?"
            icon_name     = "delete_forever"
            contex        = {'object': obj, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,contex)
    def post(self, request,id=None ,*args, **kwargs):
        context = {}
        obj = self.get_obj()
        if obj is not None:
            obj.delete()
            messages.warning(request,'Result Successfully Deleted')
            context['object']=None
            return redirect('ResultListView')
        return render(request,self.template_name,context)

class CreateResultView(View):
    template_name = "register.html"
    
    def get(self, request, *args, **kwargs):
        form = ResultCreateForm()
        header_title  = "Create Result"
        discribtion   = "Create Result for compatition"
        icon_name     = "person_add"
        contex = {'form': form, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,contex)


    def post(self, request, *args, **kwargs):
        form = ResultCreateForm(request.POST,request.FILES)
        form.status = "manual created"
        if form.is_valid():
            
            form.save()
            messages.success(request,'Your result was Create Successfully !')
            return redirect('ResultListView')
        else :
            messages.error(request,'Your result was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class ResultView(View):
    template_name = "detail.html"
    def get(self, request,id=None ,*args, **kwargs):
        if id is not None:
            obj = get_object_or_404(Result,id = id)
            context = {'object': obj}
        
        
        return render(request,self.template_name,context)

class ResultListView(View):
    template_name = "result_list.html"
    queryset = None
    queryset = Compatition.objects.get_Compatition_has_result()
  
    def get(self, request ,*args, **kwargs):
        header_title  = "Category Data Table"
        discribtion   = "Category Table "
        icon_name     = "table_chart"
        context = {'object_list':self.queryset , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)

class ResultCompatitionListView(View):
    template_name = "result_list_detail.html"
    queryset = None
    
  
    def get(self, request,id=None ,*args, **kwargs):
        #compatition = Compatition.objects.all().filter(id = id)
        compatition = Compatition.objects.get_Compatition_by_id(id = id)
        queryset = Result.objects.all().filter(compatition = compatition[0]).order_by('place')
        header_title  = "Result Compatition Data Table"
        discribtion   = "Result Compatition for " + compatition[0].name + " Compatition in " + str(compatition[0].year) +"/"+ str(compatition[0].mounth)+"/" + str(compatition[0].day)
        icon_name     = "table_chart"
        object_list   = queryset
        context = {'object_list':object_list , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
        

    



class ResultUpdateView(View):
    template_name = "create_point.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Result,id = id)
        return obj

    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = ResultCreateForm(instance=obj)
            obj = get_object_or_404(Result,id = id)
            context = {'form': form,'object':obj}

        return render(request,self.template_name,context)
    
    def post(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = ResultCreateForm(request.POST or request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            return redirect('ResultListView')
            context = {'form': form,'object':obj}
        return render(request,self.template_name,context)




class resultUploadFileView(View):
    template_name = "uploadProfile.html"
    
    def get(self, request, *args, **kwargs):
        form = ResultCsvForm()
        formc = ResultCompatitionName()
        contex = {'form': form,'formc':formc}
        return render(request,self.template_name,contex)

    # def get_isf_id(self, request, *args, **kwargs):
    #     profiles = Profile.objects.get_all_players()
    #     return 0

    def isf_id_create_or_find(self,request, first_name,last_name):
        profile = Profile.objects.get_player_by_fullname(first_name = first_name , last_name= last_name)
        if not profile:
            isf_id = self.isf_id_generator(request)
        else :
            isf_id =  profile.isf_id
        return isf_id
    def isf_id_generator(self, request, *args, **kwargs):
        profiles    = Profile.objects.get_all_players().order_by('-isf_id')[0]
        lastIsf     = profiles.isf_id
        today       =  datetime.today()
        year        = str(today.year)
        day         = str (today.day)

        if today.month < 10:
            mounth = '0' + str(today.month)
        else :
            mounth = str(today.month)

        if today.day < 10:
            day = '0' + str(today.day)
        else :
            day = str(today.day)

        new_isfid = year + mounth + day + '0000'

        if lastIsf < int(new_isfid):
            isf_id = int(new_isfid ) + 1
        else:
            isf_id = lastIsf +1
        return isf_id


    def post(self, request, *args, **kwargs):

        #compatition =Compatition.objects.filter(id = request.POST['compatition']) 
        ids = int(request.POST['compatition'])
        compatition =Compatition.objects.get_Compatition_by_id(ids)
        pointname = compatition[0].point_system_id.name
        pointSystem = Point.objects.get_point_by_name(name=pointname)[0]
        csv_file = request.FILES['data_file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request,'Only upload a CSV file')
        status = ""
        data_set = csv_file.read().decode('UTF-8')
        
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=','):
            if column[1]=='' :
                break
            else:
                isf_id = column[0]
                first_name = column[1]
                last_name = column[2]
                email = column[3]
                country_names = column[4]
                city_name = column[5]
                phone_number = column[6]
                club = column[7]
                year = column[8]
                mounth = column[9]
                day = column[10]
                id_number = column[11]
                profile_image = column[12]
                place = column[13], 
                
                
                #point = pointSystem.manual_sequence[int(place[0])]
                point = pointSystem.manual_sequence.split(',')[int(place[0])]
                
                if isf_id == '':
                    isf_id = self.isf_id_create_or_find(request,first_name = first_name,last_name=last_name)
                   
                
                if Profile.objects.get_player_by_isf_id(isf_id).exists():
                    status = "pe"
                else:
                    Profile.objects.update_or_create(   
                    isf_id = isf_id,
                    first_name = first_name ,
                    last_name = last_name,
                    email = email,
                    country_names = country_names,
                    city_name = city_name,
                    phone_number =phone_number,
                    profile_image=profile_image,
                    club = club,
                    active = True,
                    player = True ,
                    password = 123456789,
                    year = year,
                    mounth = mounth,
                    day = day,
                    id_number = id_number,
                    

                    )
                    status = status + "pc"
                if status =='pe':
                    Result.objects.update_or_create(
                    player = Profile.objects.get_player_by_isf_id(isf_id)[0],
                    compatition = compatition[0],
                    #compatition = Compatition.objects.get(name = "Marshal"),                      
                    status = 'Place Saved',
                    point = int(point),
                    place = place[0]

                )
                else :
                    Result.objects.update_or_create(
                    player = Profile.objects.get_player_by_isf_id(isf_id)[0],
                    compatition = compatition[0],        
                    status = 'Player and Place Saved',
                    point = point,
                    place = place[0]
                    )    
                          

        messages.success(request,'Your result was Create Successfully !')
        return redirect('ResultListView')
