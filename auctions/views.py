from django.shortcuts import render, redirect
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        )
from auctions.models import AuctionModel, AuctionImageModel

# Create your views here.


class AuctionListView(ListView):
    model = AuctionModel
    template_name = 'auctions/main.html'
    context_object_name = 'auctions'
    ordering = ['-start_time']

    def get_queryset(self):
        return AuctionModel.objects.filter(status = 'active').prefetch_related('images')
    

class AuctionDetailView(DetailView):
    model = AuctionModel
    template_name = 'auctions/auction_detail.html'
    context_object_name = 'auction'


class AuctionCreateView(LoginRequiredMixin, CreateView):
    model = AuctionModel
    template_name = 'auctions/auction_form.html'
    fields = ['title', 'description', 'start_price']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        auction = form.save()

        images = self.request.FILES.getlist('images')
        for image in images:
           AuctionImageModel.objects.create(auction=auction, image=image)
        return super().form_valid(form)
