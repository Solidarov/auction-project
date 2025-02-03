from django.contrib import admin
from auctions.models import AuctionModel, AuctionImageModel

# Register your models here.

class AuctionImageInline(admin.StackedInline):
    model = AuctionImageModel
    extra = 1
    max_num = 5


@admin.register(AuctionImageModel)
class LotImageAdmin(admin.ModelAdmin):
    list_display = ('auction', 'image', 'added_at')

@admin.register(AuctionModel)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_price', 'status', 'start_time')
    inlines = [
        AuctionImageInline,
    ]


    