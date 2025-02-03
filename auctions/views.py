from django.shortcuts import render
from django.views.generic import ListView, DetailView
from auctions.models import AuctionModel

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