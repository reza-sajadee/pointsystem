from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from rank_app.forms import RankCreateForm
from rank_app.models import Rank
from compatition_app.models import Compatition
from result_app.models import Result

from .forms import PlayerRankCreateForm
from .models import PlayerRank

# Create your views here.



#playerrank Classes .
class PlayerRankDeleteView(View):
    template_name = "delete.html"
    def get_obj(self):
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(PlayerRank,id = id)
        return obj
    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            header_title  = "Delete Ranking player"
            discribtion   = "do you want to delete " + obj.player_id.first_name + " " + obj.player_id.last_name + " " + obj.result_id.compatition.name + " got place " + str(obj.result_id.place) + " ?"
            icon_name     = "delete_forever"
            context       = {'object': obj, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
    def post(self, request,id=None ,*args, **kwargs):
        context = {}
        obj = self.get_obj()
        if obj is not None:
            obj.delete()
            messages.warning(request,'PlayerRank Successfully Deleted')
            context['object']=None
            return redirect('PlayerRankListView')
        return render(request,self.template_name,context)

class CreatePlayerRankView(View):
    template_name = "register.html"
    
    def get(self, request, *args, **kwargs):
        form = PlayerRankCreateForm()
        contex = {'form': form}
        return render(request,self.template_name,contex)


    def post(self, request, *args, **kwargs):
        form = PlayerRankCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your playerrank was Create Successfully !')
            return redirect('PlayerRankListView')
        else :
            messages.error(request,'Your playerrank was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class CreateRankingView(View):
    template_name = "ranking_list.html"
    
    def get(self, request, *args, **kwargs):
        form = PlayerRankCreateForm()
        header_title  = "Create Ranking"
        discribtion   = "Create your Ranking"
        icon_name     = "person_add"
        contex = {'form': form, 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,contex)


    def post(self, request, *args, **kwargs):

        form = RankCreateForm(request.POST)
        if form.is_valid():
            rank_id   = kwargs['rank']
            
            results = Result.objects.get_Result_category_date_filter(form)
            for result in results:
                if PlayerRank.objects.get_playerrank_by_player(result.player).exists():
                    player = PlayerRank.objects.get_playerrank_by_player(result.player)[0]
                    player.total = player.total + result.point
                    if player.number > rank_id.numbers:
                        pass
                    else :
                        player.best  = player.best  + result.point
                    
                    player.number = player.number +1
                    
                    player.save()
                else:
                    PlayerRank.objects.update_or_create(
                        rank_id      = rank_id,
                        result_id    = result,
                        player_id    = result.player,
                        point_id     = result.compatition.point_system_id,
                        category_id  = result.compatition.category_id,
                        total        = result.point,
                        best         = result.point,
                        number       = 1

                    )
                    

            messages.success(request,'Your Ranking was Create Successfully !')

            context = {'object_list': results}
            return render(request,self.template_name,context)
        else :
            messages.error(request,'Your playerrank was not Create  !')
        context = {'form': form}
        return render(request,self.template_name,context)

class PlayerRankView(View):
    template_name = "detail.html"
    def get(self, request,id=None ,*args, **kwargs):
        if id is not None:
            obj = get_object_or_404(PlayerRank,id = id)
            context = {'object': obj}
        
        
        return render(request,self.template_name,context)

class PlayerRankListView(View):
    template_name = "playerrank_list.html"
    queryset = None
    
    #queryset = Profile.objects.get_all_playerranks()
    def get(self, request,id=None ,*args, **kwargs):
        queryset = PlayerRank.objects.get_playerrank_by_rank_id(id).order_by('-best')
        header_title  = "Ranking Data Table"
        discribtion   = "Ranking Table " + " " + queryset[0].rank_id.category_id.name + " , " + queryset[0].rank_id.category_id.gender + " , " + queryset[0].rank_id.category_id.age + " ,for Session " + str(queryset[0].rank_id.start_year) + "/" + str(queryset[0].rank_id.start_mounth) +"/" + str(queryset[0].rank_id.start_day) + " , " +  str(queryset[0].rank_id.end_year) + "/" + str(queryset[0].rank_id.end_mounth) +"/" + str(queryset[0].rank_id.end_day) 

        icon_name     = "table_chart"
        context = {'object_list':queryset , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)
class PlayerRankUpdateView(View):
    template_name = "update.html"
    def get_obj(self):
        
        id = self.kwargs.get('id')
        obj=None
        if id is not None:
            obj = get_object_or_404(PlayerRank,id = id)
        return obj

    def get(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = PlayerRankCreateForm(instance=obj)
            obj = get_object_or_404(PlayerRank,id = id)
            context = {'form': form,'object':obj}

        return render(request,self.template_name,context)
    
    def post(self, request,id=None ,*args, **kwargs):

        obj = self.get_obj()
        if obj is not None:
            form = PlayerRankCreateForm(request.POST or request.FILES,instance=obj)
            if form.is_valid():
                form.save()
            return redirect('PlayerRankListView')
            context = {'form': form,'object':obj}
        return render(request,self.template_name,context)

class RankingListView(View):
    template_name = "ranking_list.html"
    queryset = None
    queryset = Rank.objects.all()
    #queryset = Profile.objects.get_all_ranks()
    def get(self, request,id=None ,*args, **kwargs):
        header_title  = "Rank System Data Table"
        discribtion   = "Rank System Table "
        icon_name     = "table_chart"
        context = {'object_list':self.queryset , 'header_title':header_title,'discribtion':discribtion,'icon_name':icon_name}
        return render(request,self.template_name,context)