from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from playerrank_app.views import CreateRankingView

from compatition_app.models import Compatition
from result_app.models import Result

from .forms import RankCreateForm
from .models import Rank

# Create your views here.



#rank Classes .
class RankDeleteView(View):
    template_name = "delete.html"
    def get_obj(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Rank,id = id)
        return obj
    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            header_title  = "Delete Rank System"
            discribtion   = "do you want to delete " + obj.category_id.name + " " + obj.category_id.gender + " " + obj.category_id.age + " Ranking System ?"
            icon_name     = "delete_forever"
            context       = {'object': obj, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}

        return render(request,self.template_name,context)
    def post(self, request,id=None ,*args, **kwargs):
        context = {}
        obj = self.get_obj()
        if obj is not None:
            obj.delete()
            messages.warning(request,'Rank Successfully Deleted')
            context['object']=None
            return redirect('RankListView')
        return render(request,self.template_name,context)

class CreateRankView(View):
    template_name = "register.html"
    
    def get(self, request, *args, **kwargs):
        header_title  = "Create Rank System"
        discribtion   = "Create detial of rank system"
        icon_name     = "person_add"
        form = RankCreateForm()
        contex = {'form': form, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,contex)


    def post(self, request, *args, **kwargs):
        form = RankCreateForm(request.POST,request.FILES)
        if form.is_valid():
            rank =  form.save()
            messages.success(request,'Your rank was Create Successfully !')
            return CreateRankingView.as_view()(self.request ,  rank = rank)
            #return redirect('RankListView')
        else :
            messages.error(request,'Your rank was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class RankView(View):
    template_name = "detail.html"
    def get(self, request,id=None ,*args, **kwargs):
        if id is not None:
            obj = get_object_or_404(Rank,id = id)
            context = {'object': obj}
        
        
        return render(request,self.template_name,context)

class RankListView(View):
    template_name = "rank_list.html"
    queryset = None
    queryset = Rank.objects.all()
    #queryset = Profile.objects.get_all_ranks()
    def get(self, request,id=None ,*args, **kwargs):
        header_title  = "Rank System Data Table"
        discribtion   = "Rank System Table "
        icon_name     = "table_chart"
        context = {'object_list':self.queryset , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
class RankUpdateView(View):
    template_name = "update.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(Rank,id = id)
        return obj

    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = RankCreateForm(instance=obj)
            obj = get_object_or_404(Rank,id = id)
            context = {'form': form,'object':obj}

        return render(request,self.template_name,context)
    
    def post(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = RankCreateForm(request.POST or request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            return redirect('RankListView')
            context = {'form': form,'object':obj}
        return render(request,self.template_name,context)

# class RankPlayerListView(View):
#     template_name = "rank_player_list.html"
#     queryset = None
    
#     #queryset = Profile.objects.get_all_ranks()
#     def get_ranking(self, request , id=None  ,*args, **kwargs):
#         rank = Rank.objects.get_rank_by_id(id)
#         return rank

#     def get_results_filter_category(self, request , id=None  ,*args, **kwargs):
#         rank = Rank.objects.get_rank_by_id(id)
#         results = Result.objects.get_Compatition_filter_category(id = rank.compatition.category_id.id)
#         return results

#     def get(self, request  , id=None,*args, **kwargs):
#         #queryset = Result.objects.all().filter(compatition__category_id__id = 1)
#         #results = Result.objects.get_Compatition_filter_category(category=id)
#         rank    = Rank.objects.get_rank_by_id(id)[0]
#         results = Result.objects.get_Compatition_filter_category(id = rank.category_id.id)
#         for result in results :
#             player = result.player
#             if Result.objects.all().filter(player=player).exists():
#                 pass
#             else :
#                 Rank.objects.update_or_create( 
#                      player_id      =  result.player,
#                      category_id    =  rank.category_id,
#                      start_year     =  rank.start_year,
#                      start_mounth   =  rank.start_mounth,
#                      start_day      =  rank.start_day,
#                      end_year       =  rank.end_year,
#                      end_mounth     =  rank.end_mounth,
#                      end_day        =  rank.end_day,
#                      total          =  result.point,
#                      best           =  result.point,
#                      rank           = 1,
#                      numbers        =   rank.numbers
                   
#                 )
            

#         queryset = Rank.objects.all()
#         context = {'object_list':queryset}
#         return render(request,self.template_name,context)
